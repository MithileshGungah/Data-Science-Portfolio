# AtlasWorks AI Policy Intelligence System

Enterprise AI Agent for workplace policy reasoning using Agentic RAG, LangGraph orchestration, and hybrid retrieval systems.

<img src="img/RAG_Thumbnail.jpg" alt="AtlasWorks AI Policy Intelligence System" width="880"/>

---

## Overview

AtlasWorks AI Policy Intelligence System is a sophisticated AI agent designed to answer workplace policy and compliance queries by intelligently combining internal enterprise knowledge with real-time web search.

Instead of relying on a standard retrieval-augmented generation pipeline, the system employs a structured agentic workflow. Each query is dynamically routed based on intent, contextual relevance, and retrieval confidence.

This design enables adaptive, explainable, and enterprise-ready AI responses with full execution transparency.

---

## Key Capabilities

- **Hybrid AI Routing Engine**  
  Dynamically selects between internal knowledge (RAG), external web search, or direct reasoning based on query intent and confidence scoring.

- **LangGraph Orchestration Layer**  
  Stateful multi-step execution graph with explicit routing, retrieval, evaluation, and response synthesis nodes.

- **Retrieval-Augmented Generation (RAG)**  
  Semantic search over enterprise policy documents using Pinecone vector database.

- **Retrieval Evaluation & Correction Loop**  
  Validates retrieved context before generation and triggers fallback strategies when confidence is insufficient.

- **Hybrid Knowledge Integration**  
  Combines internal documents, Tavily web search, and Groq-based LLM reasoning.

- **Execution Traceability**  
  Every request produces a structured trace of routing decisions, retrieval steps, and final response generation.

- **Modular System Architecture**  
  Clear separation between frontend interface, backend API layer, and agent reasoning core.

---

## High-Level Architecture

### End-to-End System Flow

User Query  
→ Streamlit Frontend  
→ FastAPI Backend  
→ LangGraph Agent Core  
→ Router Node (intent classification + confidence scoring)  
→ Retrieval Layer (Pinecone Vector Search) OR Web Search (Tavily)  
→ Retrieval Evaluation Node  
→ Response Synthesis (Groq LLM)  
→ Final Answer + Execution Trace

---

### System Layers

- **Frontend Layer**: Streamlit-based UI for interaction and session handling  
- **API Layer**: FastAPI backend for request orchestration and routing  
- **Agent Layer**: LangGraph-based reasoning and decision engine  
- **Knowledge Layer**: Pinecone vector database powering enterprise RAG  
- **External Tools Layer**: Tavily (web search) and Groq (LLM inference)

---

## Agent Behavior & Query Routing Examples

The following examples illustrate how AtlasWorks dynamically adapts its reasoning strategy based on retrieval confidence, document coverage, and query intent.

---

### Relevant Query → RAG-Based Response

<img src="img/Relevent_Query.png" alt="Relevant Query" width="880"/>

This case demonstrates a successful retrieval-augmented generation flow.

A query such as:
> “What types of workplace behavior are considered unacceptable at AtlasWorks?”

is correctly matched to relevant internal policy documents.

System behavior:
- Retrieves semantically relevant embeddings from Pinecone  
- Confirms sufficient context alignment  
- Generates a grounded response using the LLM  

---

### Internal Reasoning (LangGraph Decision Flow)

<img src="img/Reasoning.png" alt="Reasoning" width="880"/>

This diagram illustrates the internal orchestration logic of the LangGraph agent.

The system evaluates:
- Whether retrieved context is sufficient for RAG  
- Whether confidence thresholds are satisfied  
- Whether routing should remain in RAG or transition to fallback pathways  

This ensures deterministic, explainable reasoning rather than opaque generation.

---

### Irrelevant Query → Web Search Fallback

<img src="img/Unrelevant_Query.png" alt="Unrelevant Query" width="880"/>
<img src="img/Websearch.png" alt="Web Search" width="880"/>

When a query falls outside the scope of internal enterprise knowledge:

System behavior:
- Retrieval confidence is low or empty  
- RAG generation is rejected  
- Query is routed to external web search (Tavily)  

This ensures the system remains useful even when internal knowledge is insufficient.

---

### Relevant Query Outside Document Coverage

<img src="img/Relevant_Data_but_outside_document.png" alt="Relevant Data but outside document" width="880"/>

This scenario represents partial knowledge coverage.

Although the query is relevant to enterprise policy:
- The exact information is not present in the indexed documents  
- The system detects partial semantic overlap but insufficient grounding  

System behavior:
- Avoids hallucinated responses  
- Prevents unsupported assumptions  
- Either escalates to web search or requests clarification  

---

## System Summary

AtlasWorks AI demonstrates advanced agentic reasoning through:

- Dynamic routing between RAG, reasoning, and web search  
- Strong grounding in enterprise policy knowledge  
- Safe fallback behavior for incomplete or missing information  
- Transparent decision-making via LangGraph orchestration  
- Full traceability of every query execution path

---

## Core Modules Structure

```
agentBot/
├── frontend/
│   ├── app.py                  # Streamlit entry point
│   ├── ui_components.py       # Chat UI, toggle, trace
│   ├── backend_api.py         # API communication
│   ├── session_manager.py     # Streamlit state management
│   └── config.py              # Frontend config
│
├── backend/
│   ├── main.py                # FastAPI entry point
│   ├── agent.py               # LangGraph AI agent workflow
│   ├── vectorstore.py         # Pinecone RAG logic
│   └── config.py              # API keys and env vars
│
│
├── requirements.txt          # Python dependencies
└── .env                      # API keys (not committed)
```


---

## Technology Stack

- Python 3.9+
- FastAPI
- Streamlit
- LangGraph
- Groq (LLM inference)
- Pinecone (vector database)
- HuggingFace embeddings
- Tavily Search API
- Pydantic

---

## Setup and Installation

### Prerequisites

- Python 3.9+
- API keys for:
  - GROQ_API_KEY
  - PINECONE_API_KEY
  - TAVILY_API_KEY

---

### Installation

```bash
git clone https://github.com/your-username/atlasworks-ai-policy-assistant.git
cd atlasworks-ai-policy-assistant

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

```

### Create a .env file

```bash
GROQ_API_KEY=your_key
PINECONE_API_KEY=your_key
TAVILY_API_KEY=your_key
```

### Running the application

#### Start Backend
```bash
cd backend
python main.py
```
#### Start Frontend
```bash
cd frontend
streamlit run app.py
```
## Future Improvements

- Integrate core tools such as calculator, calendar, and code execution support
- Enable streaming LLM responses token-by-token for improved real-time experience
- Enhance RAG pipeline with reranking, multi-query retrieval, and better source grounding
- Add long-term memory with user-controlled personalization and session continuity
- Improve UI/UX with themes, smoother animations, and responsive design upgrades
