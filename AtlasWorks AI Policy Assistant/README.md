# AtlasWorks AI Policy Intelligence System

Enterprise AI Agent for workplace policy reasoning using Agentic RAG, LangGraph orchestration, and hybrid retrieval systems.

<img src="img/RAG_Thumbnail.jpg" alt="AtlasWorks AI Policy Intelligence System" width="880"/>

---

## Overview

AtlasWorks AI Policy Intelligence System is a sophisticated AI agent designed to answer workplace policy and compliance queries by intelligently combining internal enterprise knowledge with real-time web search.

The system uses a structured agentic workflow instead of a simple retrieval-augmented generation pipeline. Each query is dynamically routed based on intent, context quality, and retrieval confidence.

This enables adaptive, explainable, and enterprise-ready AI responses.

---

## Key Features

- **Hybrid AI & Intelligent Routing**  
  Dynamically selects between internal knowledge (RAG), web search, or direct reasoning based on query context.

- **LangGraph Agent Orchestration**  
  Multi-step stateful workflow with explicit routing, retrieval, evaluation, and response synthesis nodes.

- **Retrieval-Augmented Generation (RAG)**  
  Uses Pinecone vector database to perform semantic search over enterprise policy documents.

- **Retrieval Evaluation & Correction Loop**  
  Evaluates retrieved context before generation and triggers fallback web search when needed.

- **Hybrid Knowledge System**  
  Combines internal documents, external web search (Tavily), and LLM reasoning (Groq).

- **Execution Traceability**  
  Each request produces a structured trace of routing decisions, retrieval steps, and final synthesis flow.

- **Modular Architecture**  
  Clean separation between backend agent logic and frontend interface layer.

---

## High-Level Architecture

### System Flow

User Query  
→ Streamlit Frontend  
→ FastAPI Backend  
→ LangGraph Agent Core  
→ Router Node (decision engine)  
→ Vector Search (Pinecone) OR Web Search (Tavily)  
→ Retrieval Evaluation Node  
→ Response Synthesis (Groq LLM)  
→ Final Answer + Trace Output

---

### System Layers

- **Frontend Layer**: Streamlit UI for interaction and session management  
- **API Layer**: FastAPI backend handling requests and orchestration  
- **Agent Layer**: LangGraph-based reasoning engine  
- **Knowledge Layer**: Pinecone vector database for enterprise RAG  
- **External Tools**: Tavily search and Groq LLM inference  

---

## Agent Behavior & Query Routing Examples

The following examples demonstrate how the system dynamically routes queries based on retrieval confidence, document coverage, and intent classification.

---

### Relevant Query → RAG-based Response

<img src="img/Relevent_Query.png" alt="Relevant Query" width="880"/>

This example demonstrates a successful RAG retrieval flow.

A query such as:
> “What types of workplace behavior are considered unacceptable at AtlasWorks?”

is correctly matched against the internal policy corpus.

The system:
- Retrieves relevant embeddings from Pinecone
- Confirms sufficient context relevance
- Generates a grounded, document-based response using the LLM

---

### Internal Reasoning (LangGraph Decision Flow)

<img src="img/Reasoning.png" alt="Reasoning" width="880"/>

This image explains the internal LangGraph orchestration process.

The reasoning layer determines:
- Whether retrieved context is sufficient for RAG
- Whether confidence thresholds are met
- Whether routing should remain in RAG or shift to fallback mechanisms

This ensures deterministic and explainable decision-making rather than opaque LLM-only behavior.

---

### Irrelevant Query → Web Search Fallback

<img src="img/Unrelevant_Query.png" alt="Unrelevant Query" width="880"/>
<img src="img/Websearch.png" alt="Web Search" width="880"/>

For queries that are not supported by internal enterprise documents:

- Retrieval returns low or no relevant context
- The system rejects RAG-based generation
- The agent automatically routes to external web search (Tavily)

This fallback ensures the system remains useful even outside the knowledge boundary of the internal dataset.

---

### Relevant Query Outside Document Coverage

<img src="img/Relevant_Data_but_outside_document.png" alt="Relevant Data but outside document" width="880"/>

This case highlights a partial-match scenario.

The query is related to enterprise policy but:
- The exact information is not present in the indexed documents
- The system detects partial relevance but insufficient grounding

In this case, the system avoids hallucination and:
- Does not fabricate answers
- Either requests clarification or escalates to external search
- Maintains response safety and factual integrity

---

## System Summary

AtlasWorks AI demonstrates advanced agentic behavior through:

- Dynamic routing between RAG, reasoning, and web search  
- Strong grounding in enterprise policy data  
- Safe fallback behavior for unknown or missing information  
- Transparent decision-making via LangGraph orchestration  
- Full traceability of execution flow per query

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
