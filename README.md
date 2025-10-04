# RFP Response Generator

AI agent system that automates RFP responses using LangGraph multi-agent architecture with RAG (ChromaDB + Cohere reranking).

## Features

- Multi-agent workflow with LangGraph (extractor → researcher → generator)
- Advanced RAG: ChromaDB vector DB + Cohere reranking
- Generates answers with confidence scores
- RAGAS evaluation (faithfulness, relevancy, context precision)
- FastAPI REST API
- Streamlit testing interface

## Tech Stack

Python 3.12, LangGraph, ChromaDB, Cohere, OpenAI GPT-4o-mini, RAGAS, FastAPI, Streamlit

## Installation

```bash
git clone <repo-url>
cd rfp_generator
uv venv && source .venv/bin/activate
uv pip install -r requirements.txt
```

Create `.env`:
```
OPENAI_API_KEY=your_key
COHERE_API_KEY=your_key
```

## Usage

**Setup knowledge base:**
```bash
python main.py
```

**Start API:**
```bash
python -m uvicorn api.main:app --reload
```

**Launch GUI:**
```bash
streamlit run streamlit_app.py
```

Access Streamlit at http://localhost:8501

## Evaluation

Current RAGAS scores:
- Faithfulness: 0.73
- Answer Relevancy: 0.96
- Context Precision: 0.67

Run evaluation:
```bash
python tests/ragas_eval.py
```

## Architecture

- **Supervisor**: Routes workflow based on state
- **Extractor**: Regex-based question extraction from RFPs
- **Researcher**: RAG retrieval (15 candidates → rerank to top 5)
- **Generator**: LLM generates structured answers with trust scores

State flows through LangGraph with TypedDict schemas. Multi-tenancy via LangGraph Store.
