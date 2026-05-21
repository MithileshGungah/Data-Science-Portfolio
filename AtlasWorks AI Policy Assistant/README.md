# AtlasWorks AI Policy Intelligence System

Enterprise-grade AI assistant for workplace policy reasoning using Agentic RAG, LangGraph orchestration, and hybrid retrieval systems.

---

## Overview

AtlasWorks AI Policy Intelligence System is an AI agent designed to answer internal policy and compliance queries using a structured reasoning pipeline.

It combines:

- Internal knowledge base (Pinecone vector database)
- Real-time web search (Tavily)
- LLM reasoning (Groq)
- Multi-step agent orchestration (LangGraph)

Instead of a single retrieval-and-response flow, the system uses a decision-based architecture that dynamically selects the best information source for each query.

---

## Key Features

### Agentic RAG System
The system routes queries dynamically between:
- Vector-based internal knowledge retrieval
- Web search fallback for external information
- Direct LLM reasoning when appropriate

---

### LangGraph Orchestration
The assistant is implemented as a stateful graph where each node represents a reasoning step such as routing, retrieval, evaluation, and synthesis.

This enables:
- Multi-step controlled reasoning
- Explicit decision flow
- Traceable execution paths
- Stateful agent behavior

---

### Enterprise Knowledge Retrieval
Uses Pinecone vector database to store and retrieve enterprise policy documents using semantic search.

This allows:
- Context-aware retrieval
- Semantic understanding of queries
- Scalable document indexing

---

### Retrieval Evaluation Layer
The system evaluates retrieved context before using it in the final answer.

If the context is insufficient:
- It triggers web search
- Or adjusts retrieval strategy
- Or re-runs reasoning flow

---

### Hybrid Knowledge System
Combines:
- Internal enterprise documents
- External web search results
- LLM reasoning layer

This ensures both accuracy and freshness of responses.

---

### Observability
Each request generates a trace including:
- routing decision
- retrieval step
- web search usage
- evaluation outcome
- final synthesis step

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

## Backend Structure

- agent.py → LangGraph agent workflow and routing logic
- main.py → FastAPI entry point
- vectortore.py → Pinecone vector retrieval implementation
- config.py → Environment and API configuration

Backend responsibilities:
- Query orchestration
- Retrieval pipeline execution
- Web search fallback logic
- API endpoints

---

## Frontend Structure

- app.py → Frontend application entry point
- backend_api.py → Backend communication layer
- session_manager.py → Conversation and session handling
- ui_components.py → UI building components
- config.py → Frontend configuration

Frontend responsibilities:
- User interface for querying
- Session management
- API integration
- UI state handling

---

## Tech Stack

FastAPI, LangGraph, Groq, Pinecone, HuggingFace Embeddings, Tavily API, Pydantic

---

## System Design Highlights

- Multi-step agentic architecture instead of linear RAG
- Explicit routing between multiple knowledge sources
- Separation of retrieval, reasoning, and synthesis layers
- Stateful graph-based AI orchestration
- Hybrid internal and external knowledge system
- Observability-driven execution tracking

---

## Why This Project Is Different

Traditional RAG systems:

Retrieve → Generate

This system:

Reason → Route → Retrieve → Evaluate → Generate

This enables adaptive decision-making and improves reliability in enterprise environments.

---

## Run Locally

Backend:
python main.py

Frontend:
python app.py

API Docs:
http://localhost:8000/docs

---

## API

POST /chat

Request:
{
  "query": "What is the remote work policy?"
}

---

POST /upload-document

Uploads and indexes enterprise documents into the vector database.

---

## Project Summary

Built an enterprise AI Policy Intelligence System using LangGraph, FastAPI, and Pinecone.

Implemented an agentic RAG architecture with dynamic routing between internal knowledge retrieval and web search, including retrieval evaluation and multi-step reasoning workflows.

Designed a modular system with clear separation between agent logic, API layer, and frontend interface.
