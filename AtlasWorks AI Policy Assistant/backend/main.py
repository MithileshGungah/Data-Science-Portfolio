# rag_agent_app/backend/main.py

import os
import time
from typing import List, Dict, Any
import tempfile

from fastapi import FastAPI, HTTPException, status, UploadFile, File
from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.checkpoint.memory import MemorySaver
from langchain_community.document_loaders import PyPDFLoader

from agent import rag_agent
from vectorstore import add_document_to_vectorstore

# FastAPI application initialization
app = FastAPI(
    title="LangGraph RAG Agent API",
    description="API for the LangGraph-powered RAG agent with Pinecone and Groq.",
    version="1.0.0",
)

# In-memory checkpoint store (used for session state tracking)
memory = MemorySaver()

# Request/response schemas for API communication
class TraceEvent(BaseModel):
    step: int
    node_name: str
    description: str
    details: Dict[str, Any] = Field(default_factory=dict)
    event_type: str

class QueryRequest(BaseModel):
    session_id: str
    query: str
    enable_web_search: bool = True  # Controls whether web search is enabled per request

class AgentResponse(BaseModel):
    response: str
    trace_events: List[TraceEvent] = Field(default_factory=list)

class DocumentUploadResponse(BaseModel):
    message: str
    filename: str
    processed_chunks: int

# Endpoint for uploading and indexing PDF documents into the vector store
@app.post("/upload-document/", response_model=DocumentUploadResponse, status_code=status.HTTP_200_OK)
async def upload_document(file: UploadFile = File(...)):
    """
    Accepts a PDF file, extracts its text, and stores it in the RAG knowledge base.
    """
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF files are supported."
        )

    # Save uploaded file temporarily for processing
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        file_content = await file.read()
        tmp_file.write(file_content)
        temp_file_path = tmp_file.name

    print(f"Received PDF: {file.filename}, saved to {temp_file_path}")

    try:
        # Load and parse PDF content
        loader = PyPDFLoader(temp_file_path)
        documents = loader.load()

        total_chunks_added = 0

        # Convert extracted text into vector store embeddings
        if documents:
            full_text_content = "\n\n".join([doc.page_content for doc in documents])
            add_document_to_vectorstore(full_text_content)
            total_chunks_added = len(documents)

        return DocumentUploadResponse(
            message=f"PDF '{file.filename}' successfully uploaded and indexed.",
            filename=file.filename,
            processed_chunks=total_chunks_added
        )

    except Exception as e:
        print(f"Error processing PDF: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to process PDF: {e}"
        )

    finally:
        # Cleanup temporary file after processing
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
            print(f"Removed temporary file: {temp_file_path}")

# Chat endpoint for interacting with the RAG agent
@app.post("/chat/", response_model=AgentResponse)
async def chat_with_agent(request: QueryRequest):
    trace_events_for_frontend: List[TraceEvent] = []

    try:
        # Pass session and feature flags into LangGraph runtime config
        config = {
            "configurable": {
                "thread_id": request.session_id,
                "web_search_enabled": request.enable_web_search
            }
        }

        # Initialize input message for the agent
        inputs = {"messages": [HumanMessage(content=request.query)]}

        final_message = ""

        print(f"Starting agent session: {request.session_id}")
        print(f"Web search enabled: {request.enable_web_search}")

        # Stream execution of LangGraph nodes
        for i, s in enumerate(rag_agent.stream(inputs, config=config)):
            current_node_name = None
            node_output_state = None

            # Extract node execution output
            if '__end__' in s:
                current_node_name = '__end__'
                node_output_state = s['__end__']
            else:
                current_node_name = list(s.keys())[0]
                node_output_state = s[current_node_name]

            event_description = f"Executing node: {current_node_name}"
            event_details = {}
            event_type = "generic_node_execution"

            # Router node trace formatting
            if current_node_name == "router":
                route_decision = node_output_state.get('route')
                initial_decision = node_output_state.get('initial_router_decision', route_decision)
                override_reason = node_output_state.get('router_override_reason', None)

                if override_reason:
                    event_description = (
                        f"Router decision overridden from '{initial_decision}' to '{route_decision}'."
                    )
                    event_details = {
                        "initial_decision": initial_decision,
                        "final_decision": route_decision,
                        "override_reason": override_reason
                    }
                else:
                    event_description = f"Router decision: '{route_decision}'"
                    event_details = {"decision": route_decision}

                event_type = "router_decision"

            # RAG node trace formatting
            elif current_node_name == "rag_lookup":
                rag_content_summary = node_output_state.get("rag", "")[:200] + "..."
                rag_sufficient = node_output_state.get("route") == "answer"

                if rag_sufficient:
                    event_description = "RAG retrieval sufficient. Proceeding to answer."
                    event_details = {
                        "retrieved_content_summary": rag_content_summary,
                        "sufficiency": "sufficient"
                    }
                else:
                    event_description = "RAG retrieval insufficient. Redirecting to web search."
                    event_details = {
                        "retrieved_content_summary": rag_content_summary,
                        "sufficiency": "insufficient"
                    }

                event_type = "rag_action"

            # Web search node trace formatting
            elif current_node_name == "web_search":
                web_content_summary = node_output_state.get("web", "")[:200] + "..."
                event_description = "Web search executed and results retrieved."
                event_details = {"retrieved_content_summary": web_content_summary}
                event_type = "web_action"

            # Answer generation node trace formatting
            elif current_node_name == "answer":
                event_description = "Generating final response using collected context."
                event_type = "answer_generation"

            # Completion event
            elif current_node_name == "__end__":
                event_description = "Agent execution completed."
                event_type = "process_end"

            # Append structured trace event
            trace_events_for_frontend.append(
                TraceEvent(
                    step=i + 1,
                    node_name=current_node_name,
                    description=event_description,
                    details=event_details,
                    event_type=event_type
                )
            )

            print(f"Step {i+1}: {current_node_name} -> {event_description}")

        # Extract final message from last state
        final_actual_state_dict = None

        if s:
            if '__end__' in s:
                final_actual_state_dict = s['__end__']
            else:
                final_actual_state_dict = s.get(list(s.keys())[0])

        if final_actual_state_dict and "messages" in final_actual_state_dict:
            for msg in reversed(final_actual_state_dict["messages"]):
                if isinstance(msg, AIMessage):
                    final_message = msg.content
                    break

        # Validate final output
        if not final_message:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="No valid AI response generated."
            )

        print(f"Final response generated: {final_message[:200]}...")

        return AgentResponse(
            response=final_message,
            trace_events=trace_events_for_frontend
        )

    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"Chat error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error: {e}"
        )

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}