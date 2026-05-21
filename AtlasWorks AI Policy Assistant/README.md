# AtlasWorks AI Policy Intelligence System

Enterprise-grade AI assistant for workplace policy reasoning using Agentic RAG, LangGraph orchestration, and hybrid retrieval systems.

---

## System Architecture

- Streamlit Frontend (UI Layer)  
- FastAPI Backend (API Layer)  
- LangGraph Agent (Orchestration Layer)  
- Router Node (Decision Engine)  
- Vector Search (Pinecone) OR Web Search (Tavily)  
- Retrieval Evaluation Node  
- Response Synthesis (Groq LLM)  
- Final Answer + Execution Trace

---

## Overview

AtlasWorks AI Policy Intelligence System is an AI agent designed to answer workplace policy and compliance queries using a structured multi-step reasoning architecture.

Instead of a single retrieval-and-generation pipeline, the system uses an agentic decision flow that dynamically selects between internal knowledge, external web search, and LLM reasoning based on query intent and retrieval quality.

This enables a more adaptive and reliable enterprise AI system.

---

## Why This System Is Different

Traditional RAG systems:

Retrieve → Generate

This system uses a decision-driven reasoning architecture:

Reason → Route → Retrieve → Evaluate → Generate

This allows the agent to behave like a structured AI system rather than a static chatbot.

---

## System Capabilities

### Agentic RAG Workflow

The system dynamically routes each query through:

- Internal knowledge retrieval using Pinecone vector database
- External web search using Tavily API
- Direct LLM reasoning when appropriate

This replaces static RAG with a decision-driven pipeline.

---

### LangGraph Orchestration

The AI agent is implemented as a stateful graph where each node represents a reasoning step.

Key properties:

- Multi-step execution flow
- Stateful transitions between nodes
- Explicit routing decisions
- Fully traceable reasoning path

Core stages:
routing → retrieval → evaluation → synthesis

---

### Enterprise Knowledge Retrieval

The system uses Pinecone vector database to store and retrieve enterprise policy documents using semantic embeddings.

Capabilities:

- Semantic search over internal documents
- Context-aware retrieval beyond keyword matching
- Scalable knowledge indexing

---

### Retrieval Evaluation & Correction

Before generating a final response, retrieved context is evaluated for relevance and completeness.

If context is insufficient:

- Web search is triggered
- Retrieval strategy is adjusted
- Reasoning flow is re-evaluated

This introduces a self-correcting retrieval loop.

---

### Hybrid Knowledge System

The system integrates:

- Internal enterprise knowledge (Pinecone)
- External web search (Tavily)
- LLM reasoning layer (Groq)

This ensures both accuracy and real-time relevance.

---

### Observability & Traceability

Each request generates a full execution trace including:

- routing decision
- retrieval source selection
- web search usage
- evaluation outcome
- final response path

---

## Key Design Principles

- Separation of reasoning, retrieval, and generation
- Graph-based agent orchestration
- Hybrid knowledge sources (internal and external)
- Self-correcting retrieval mechanism
- Stateful execution flow
- Observability-first design

---

## Tech Stack

FastAPI, LangGraph, Groq, Pinecone, HuggingFace Embeddings, Tavily API, Streamlit, Pydantic

---

## Core Modules Structure

## 📦 Core Modules Structure

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

## ⚙️ Technology Stack

- **Language**: Python 3.9+
- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Agent Orchestration**: LangGraph
- **LLMs & Tools**: LangChain, Groq (Llama 3)
- **Embeddings**: sentence-transformers/all-MiniLM-L6-v2
- **Vector Store**: Pinecone
- **PDF Processing**: PyPDFLoader
- **Search Engine**: Tavily API
