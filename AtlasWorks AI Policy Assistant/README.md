# AtlasWorks AI Policy Intelligence System

Enterprise-grade AI assistant for workplace policy reasoning using Agentic RAG, LangGraph orchestration, and hybrid retrieval systems.

---

## Overview

AtlasWorks AI Policy Intelligence System is an AI agent designed to answer workplace policy and compliance queries using a structured, multi-step reasoning workflow.

The system combines:

- Internal enterprise knowledge (Pinecone vector database)
- Real-time web search (Tavily API)
- LLM reasoning (Groq)
- Agentic orchestration (LangGraph)

Instead of a single-pass RAG pipeline, the system uses a decision-driven architecture that dynamically selects the best information source for each query and evaluates retrieval quality before generating a response.

---

## Key Features

### Agentic RAG System
Dynamically routes queries between:
- Internal vector-based knowledge retrieval
- Web search fallback for external context
- Direct LLM reasoning when appropriate

---

### LangGraph Orchestration
Implements a stateful graph-based AI workflow where each node represents a reasoning stage such as routing, retrieval, evaluation, and synthesis.

This enables:
- Multi-step controlled reasoning
- Explicit execution flow
- Stateful agent behavior
- Traceable decision paths

---

### Enterprise Knowledge Retrieval
Uses Pinecone vector database for semantic retrieval of enterprise policy documents.

Capabilities:
- Semantic search over policy data
- Context-aware retrieval
- Scalable knowledge indexing

---

### Retrieval Evaluation Layer
Evaluates retrieved context before using it in the final response.

If context is insufficient:
- Web search is triggered
- Retrieval strategy is adjusted
- Reasoning flow is re-evaluated

---

### Hybrid Knowledge System
Combines:
- Internal enterprise knowledge
- External web search results
- LLM reasoning layer

Ensures both accuracy and real-time relevance.

---

### Observability
Each request generates an execution trace including:
- routing decision
- retrieval step
- web search usage
- evaluation outcome
- final synthesis path

---

## System Architecture

User Query  
→ LangGraph Agent  
→ Router Node  
→ Vector Search (Pinecone) OR Web Search (Tavily)  
→ Retrieval Evaluation Node  
→ Response Synthesis (Groq LLM)  
→ Final Answer + Trace

---

## Core Modules Structure

atlasworks-ai-policy-assistant/
```
│
├── backend/
│   ├── agent.py              # LangGraph agent (routing, retrieval, synthesis workflow)
│   ├── main.py               # FastAPI entry point (API routes, server startup)
│   ├── vectortore.py         # Pinecone vector store integration (RAG retrieval layer)
│   ├── config.py             # Environment variables and API key configuration
│
├── frontend/
│   ├── app.py                # Frontend application entry point (UI runtime)
│   ├── backend_api.py        # API communication layer between frontend and backend
│   ├── session_manager.py    # Session state and conversation memory handling
│   ├── ui_components.py      # Reusable UI components and layout elements
│   ├── config.py             # Frontend configuration settings
│
├── requirements.txt          # Python dependencies
└── .env                      # Environment variables (not committed)
```
