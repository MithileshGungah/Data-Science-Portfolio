# rag_agent_app/backend/agent.py

import os
from typing import List, Literal, TypedDict
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from pydantic import BaseModel, Field
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.runnables import RunnableConfig  # Enables runtime configuration injection

# Import API keys and vector retriever
from config import GROQ_API_KEY, TAVILY_API_KEY
from vectorstore import get_retriever

# Environment setup for external tools
os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY
tavily = TavilySearch(max_results=3, topic="general")

@tool
def web_search_tool(query: str) -> str:
    """Performs web search using Tavily and formats results."""
    try:
        result = tavily.invoke({"query": query})
        if isinstance(result, dict) and 'results' in result:
            formatted_results = []
            for item in result['results']:
                title = item.get('title', 'No title')
                content = item.get('content', 'No content')
                url = item.get('url', '')
                formatted_results.append(f"Title: {title}\nContent: {content}\nURL: {url}")
            return "\n\n".join(formatted_results) if formatted_results else "No results found"
        else:
            return str(result)
    except Exception as e:
        return f"WEB_ERROR::{e}"

@tool
def rag_search_tool(query: str) -> str:
    """Retrieves top-k relevant document chunks from the vector database."""
    try:
        retriever_instance = get_retriever()
        docs = retriever_instance.invoke(query, k=5)
        return "\n\n".join(d.page_content for d in docs) if docs else ""
    except Exception as e:
        return f"RAG_ERROR::{e}"

# Structured routing decision schema for the LLM router
class RouteDecision(BaseModel):
    route: Literal["rag", "web", "answer", "end"]
    reply: str | None = Field(None, description="Used only when route == 'end'")

# Structured judgment schema for RAG sufficiency evaluation
class RagJudge(BaseModel):
    sufficient: bool = Field(..., description="Indicates whether retrieved context is sufficient")

# Configure Groq LLM API key
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# Router model responsible for deciding execution path
router_llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
).with_structured_output(RouteDecision)

# Judge model that evaluates retrieved RAG context quality
judge_llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
).with_structured_output(RagJudge)

# Final answer generation model
answer_llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)

# Shared state definition across all graph nodes
class AgentState(TypedDict, total=False):
    messages: List[BaseMessage]
    route: Literal["rag", "web", "answer", "end"]
    rag: str
    web: str
    web_search_enabled: bool  # Controls whether web search is allowed

# Router node: determines next step based on query and config
def router_node(state: AgentState, config: RunnableConfig) -> AgentState:
    print("\n--- Entering router_node ---")

    # Extract latest user query
    query = next((m.content for m in reversed(state["messages"]) if isinstance(m, HumanMessage)), "")

    # Read runtime flag for web search capability
    web_search_enabled = config.get("configurable", {}).get("web_search_enabled", True)
    print(f"Router received web search info : {web_search_enabled}")

    # Base instruction for routing decisions
    system_prompt = (
        "You are an intelligent routing agent designed to direct user queries to the most appropriate tool."
        "Your primary goal is to provide accurate and relevant information by selecting the best source."
        "Prioritize using the **internal knowledge base (RAG)** for factual information that is likely "
        "to be contained within pre-uploaded documents or for common, well-established facts."
    )

    # Extend prompt with web-enabled routing rules
    if web_search_enabled:
        system_prompt += (
            "You **CAN** use web search for queries requiring real-time or recent information."
            "\n\nChoose one of the following routes:"
            "\n- 'rag': Use internal knowledge base for factual or static information."
            "\n- 'web': Use for real-time, breaking, or highly dynamic information."
        )
    else:
        system_prompt += (
            "**Web search is disabled.** Do not select 'web'."
            "\n\nChoose one of the following routes:"
            "\n- 'rag': Use internal knowledge base or general knowledge."
            "\n- 'answer': For simple questions that require no retrieval."
        )

    system_prompt += (
        "\n- 'answer': For simple direct responses without retrieval."
        "\n- 'end': For greetings or conversational replies."
    )

    messages = [
        ("system", system_prompt),
        ("user", query)
    ]

    # Get routing decision from LLM
    result: RouteDecision = router_llm.invoke(messages)

    initial_router_decision = result.route
    router_override_reason = None

    # Prevent web routing if disabled
    if not web_search_enabled and result.route == "web":
        result.route = "rag"
        router_override_reason = "Web search disabled; redirected to RAG."
        print("Router override: web -> rag due to disabled setting.")

    print(f"Router final decision: {result.route}, Reply: {result.reply}")

    out = {
        "messages": state["messages"],
        "route": result.route,
        "web_search_enabled": web_search_enabled
    }

    # Track override metadata for debugging
    if router_override_reason:
        out["initial_router_decision"] = initial_router_decision
        out["router_override_reason"] = router_override_reason

    # Handle direct conversational exit
    if result.route == "end":
        out["messages"] = state["messages"] + [AIMessage(content=result.reply or "Hello!")]

    print("--- Exiting router_node ---")
    return out

# RAG retrieval node: fetches and evaluates internal knowledge
def rag_node(state: AgentState, config: RunnableConfig) -> AgentState:
    print("\n--- Entering rag_node ---")

    # Extract user query
    query = next((m.content for m in reversed(state["messages"]) if isinstance(m, HumanMessage)), "")

    # Read runtime configuration
    web_search_enabled = config.get("configurable", {}).get("web_search_enabled", True)
    print(f"Router received web search info : {web_search_enabled}")
    print(f"RAG query: {query}")

    # Retrieve relevant document chunks
    chunks = rag_search_tool.invoke(query)

    # Handle retrieval failure
    if chunks.startswith("RAG_ERROR::"):
        print("RAG error encountered")
        next_route = "web" if web_search_enabled else "answer"
        return {**state, "rag": "", "route": next_route}

    # Log retrieved content
    if chunks:
        print(f"Retrieved chunks: {chunks[:500]}...")
    else:
        print("No RAG results found")

    # Evaluate sufficiency of retrieved context
    judge_messages = [
        ("system", (
            "Evaluate whether retrieved context fully answers the question."
        )),
        ("user", f"Question: {query}\nContext: {chunks}")
    ]

    verdict: RagJudge = judge_llm.invoke(judge_messages)
    print(f"RAG sufficiency: {verdict.sufficient}")

    # Decide next step based on evaluation and config
    if verdict.sufficient:
        next_route = "answer"
    else:
        next_route = "web" if web_search_enabled else "answer"

    print("--- Exiting rag_node ---")

    return {
        **state,
        "rag": chunks,
        "route": next_route,
        "web_search_enabled": web_search_enabled
    }

# Web search node: retrieves external information when needed
def web_node(state: AgentState, config: RunnableConfig) -> AgentState:
    print("\n--- Entering web_node ---")

    query = next((m.content for m in reversed(state["messages"]) if isinstance(m, HumanMessage)), "")

    web_search_enabled = config.get("configurable", {}).get("web_search_enabled", True)
    print(f"Router received web search info : {web_search_enabled}")

    # Skip execution if disabled
    if not web_search_enabled:
        print("Web search disabled; skipping execution.")
        return {**state, "web": "Web search disabled.", "route": "answer"}

    print(f"Web search query: {query}")

    # Execute Tavily search
    snippets = web_search_tool.invoke(query)

    # Handle API failure
    if snippets.startswith("WEB_ERROR::"):
        print("Web search error encountered")
        return {**state, "web": "", "route": "answer"}

    print(f"Web results retrieved: {snippets[:200]}...")
    print("--- Exiting web_node ---")

    return {**state, "web": snippets, "route": "answer"}

# Final answer generation node using combined context
def answer_node(state: AgentState) -> AgentState:
    print("\n--- Entering answer_node ---")

    # Extract latest user query
    user_q = next((m.content for m in reversed(state["messages"]) if isinstance(m, HumanMessage)), "")

    # Build context from available sources
    ctx_parts = []
    if state.get("rag"):
        ctx_parts.append("Knowledge Base:\n" + state["rag"])
    if state.get("web") and not state["web"].startswith("Web search was disabled"):
        ctx_parts.append("Web Results:\n" + state["web"])

    context = "\n\n".join(ctx_parts)

    # Fallback when no context exists
    if not context.strip():
        context = "No external context available."

    # Construct prompt for final response generation
    prompt = f"""Answer the question using the context.

Question: {user_q}

Context:
{context}
"""

    print(f"Answer prompt prepared: {prompt[:500]}...")

    # Generate final response
    ans = answer_llm.invoke([HumanMessage(content=prompt)]).content

    print(f"Generated answer: {ans[:200]}...")

    print("--- Exiting answer_node ---")

    return {
        **state,
        "messages": state["messages"] + [AIMessage(content=ans)]
    }

# Routing helpers for graph transitions
def from_router(st: AgentState) -> Literal["rag", "web", "answer", "end"]:
    return st["route"]

def after_rag(st: AgentState) -> Literal["answer", "web"]:
    return st["route"]

def after_web(_) -> Literal["answer"]:
    return "answer"

# Graph construction and compilation
def build_agent():
    g = StateGraph(AgentState)

    # Register nodes
    g.add_node("router", router_node)
    g.add_node("rag_lookup", rag_node)
    g.add_node("web_search", web_node)
    g.add_node("answer", answer_node)

    # Define entry point
    g.set_entry_point("router")

    # Router-based routing logic
    g.add_conditional_edges(
        "router",
        from_router,
        {
            "rag": "rag_lookup",
            "web": "web_search",
            "answer": "answer",
            "end": END
        }
    )

    # Post-RAG routing logic
    g.add_conditional_edges(
        "rag_lookup",
        after_rag,
        {
            "answer": "answer",
            "web": "web_search"
        }
    )

    # Web leads to final answer
    g.add_edge("web_search", "answer")

    # End execution after answer generation
    g.add_edge("answer", END)

    # Compile graph with in-memory checkpointing
    agent = g.compile(checkpointer=MemorySaver())
    return agent

# Instantiate final RAG agent
rag_agent = build_agent()