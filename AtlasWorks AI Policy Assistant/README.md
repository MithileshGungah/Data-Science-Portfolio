# AtlasWorks AI Policy Intelligence System

Enterprise-grade AI assistant for workplace policy reasoning using Agentic RAG, LangGraph orchestration, and hybrid retrieval systems.

---

## Overview

AtlasWorks AI Policy Intelligence System is an AI agent designed to answer workplace policy and compliance queries through a structured, multi-step reasoning architecture.

Instead of relying on a single retrieval-and-response pipeline, the system uses an **agentic decision flow** that dynamically selects between internal knowledge, external web search, and direct reasoning based on query intent and retrieval quality.

This enables more reliable, adaptive, and context-aware enterprise responses.

---

## System Capabilities

### 1. Agentic RAG Workflow

The system dynamically routes each query through multiple reasoning paths:

- Internal knowledge retrieval using vector search
- External web search for missing or outdated information
- Direct LLM reasoning when retrieval is unnecessary

This replaces static RAG with a decision-driven AI pipeline.

---

### 2. LangGraph-Based Orchestration

The AI agent is implemented as a **stateful execution graph** where each node represents a reasoning stage.

Key properties:

- Explicit control over execution flow
- Multi-step reasoning pipeline
- Stateful transitions between nodes
- Traceable decision-making process

Core stages include:
routing → retrieval → evaluation → synthesis

---

### 3. Enterprise Knowledge Retrieval (RAG Layer)

The system uses Pinecone as a vector database to store and retrieve enterprise policy documents using semantic embeddings.

This enables:

- Semantic search over internal documents
- Context-aware retrieval beyond keyword matching
- Scalable enterprise knowledge indexing

---

### 4. Retrieval Evaluation & Correction

Before generating a final response, retrieved context is evaluated for relevance and completeness.

If the context is insufficient:

- Web search is triggered
- Retrieval strategy is adjusted
- Reasoning flow is re-evaluated

This introduces a **self-correcting retrieval mechanism**.

---

### 5. Hybrid Knowledge System

The system integrates multiple information sources:

- Internal enterprise knowledge (Pinecone)
- External web search (Tavily API)
- LLM reasoning layer (Groq)

This ensures both factual grounding and real-time relevance.

---

### 6. Observability & Traceability

Each request generates a full execution trace including:

- routing decision
- retrieval source selection
- web search activation
- evaluation outcome
- final synthesis path

This makes the system fully debuggable and auditable.

---

## System Architecture

User Query  
→ LangGraph Agent  
→ Router Node (decision making)  
→ Vector Search (Pinecone) OR Web Search (Tavily)  
→ Retrieval Evaluation Node  
→ Response Synthesis (Groq LLM)  
→ Final Answer + Execution Trace

---

## Core Modules Structure
```
atlasworks-ai-policy-assistant/
│
├── backend/
│ ├── agent.py # LangGraph agent (routing, retrieval, synthesis workflow)
│ ├── main.py # FastAPI entry point (API routes, server startup)
│ ├── vectortore.py # Pinecone vector retrieval layer (RAG engine)
│ ├── config.py # Environment variables and configuration
│
├── frontend/
│ ├── app.py # Frontend application entry point
│ ├── backend_api.py # Backend API communication layer
│ ├── session_manager.py # Conversation state and session handling
│ ├── ui_components.py # UI components and layout system
│ ├── config.py # Frontend configuration settings
│
├── requirements.txt
└── .env
```


---

## Why This System Is Different

Traditional RAG systems:

Retrieve → Generate

This system implements a **decision-driven reasoning architecture**:

Reason → Route → Retrieve → Evaluate → Generate

This allows the agent to behave more like a structured AI system rather than a static chatbot.

---

## Tech Stack

FastAPI, LangGraph, Groq, Pinecone, HuggingFace Embeddings, Tavily API, Pydantic

---

## Key Design Principles

- Separation of reasoning, retrieval, and generation
- Graph-based agent orchestration
- Hybrid knowledge sources (internal + external)
- Self-correcting retrieval mechanism
- Stateful execution flow
- Observability-first design
