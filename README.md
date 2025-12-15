# Multi-Agent LangGraph Boilerplate (OpenAI)

Python starter project for a simple LangGraph multi-agent workflow with:

- **Supervisor** node that routes the request
- **RAG agent** that answers using retrieved context
- **API agent** that simulates/executes an API call

The default example indexes a small built-in document into a local Chroma vector store and routes queries based on similarity score.

## Prerequisites

- Python 3.10+
- An OpenAI API key

## Setup

1. Create and activate a virtualenv:
   - `python -m venv .venv`
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
2. Install dependencies:
   - `python -m pip install -r requirements.txt`
3. Create your env file:
   - `cp .env.example .env` (Windows PowerShell: `copy .env.example .env`)

## Configuration

Environment variables (loaded from `.env` via Pydantic Settings in `src/multi_agent/config.py`):

- `OPENAI_API_KEY` (required)
- `OPENAI_MODEL` (default: `gpt-4o-mini`)
- `EMBEDDING_MODEL` (default: `text-embedding-3-small`)

## Usage

### 1) Index sample data (RAG)

Indexes the built-in `rag_text` into `./vector_store`:

- `python run.py --index`

### 2) Ask a question

- `python run.py --question "What is the AI singularity?"`

### 3) Interactive mode

- `python run.py`

### Optional: run as an installed module

If you prefer module execution, install editable and run:

- `python -m pip install -e .`
- `python -m multi_agent.main --question "What is the AI singularity?"`

## How it works

- Graph wiring: `src/multi_agent/graph.py`
  - Entry: `supervisor`
  - Route to: `rag_agent` or `api_agent`
- Supervisor routing logic: `src/multi_agent/nodes/supervisor/node.py`
  - Runs a vector search and chooses the next node
- RAG response generation: `src/multi_agent/nodes/rag/node.py`
- API agent: `src/multi_agent/nodes/api/node.py`

## Notes

- The vector store is persisted under `./vector_store` (ignored by git). Delete that folder to reset the index.
- `api_agent` performs a real HTTP request (see `src/multi_agent/nodes/api/node.py`); it needs network access at runtime.
