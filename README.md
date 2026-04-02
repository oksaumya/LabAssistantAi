# Lab Assistant AI

A RAG-based AI chatbot for the CSE department's Advanced AI & Deep Learning Lab. Students can ask questions about lab timings, hardware, coursework, policies, and troubleshooting — and get accurate, context-grounded answers powered by the Grok API.

## Tech Stack

- **Backend:** Python, FastAPI
- **LLM:** Grok API (xAI) — `grok-3-mini`
- **RAG Pipeline:** LangChain + ChromaDB + sentence-transformers
- **Frontend:** HTML / CSS / JavaScript (SSE streaming)

## Project Structure

```
LabAssistantAi/
├── .env                       # Grok API key (gitignored)
├── config.py                  # Settings (API URL, model name, system prompt)
├── rag.py                     # RAG pipeline (embedding, vector store, chain)
├── main.py                    # FastAPI server with SSE streaming endpoint
├── requirements.txt           # Python dependencies
├── knowledge_base/
│   └── lab_manual.md          # Lab knowledge base document
└── static/
    ├── index.html             # Chat UI
    ├── style.css              # Dark theme styling
    └── script.js              # Chat logic with SSE streaming
```

## Setup

### Prerequisites

- Python 3.10+
- A Grok API key from [console.x.ai](https://console.x.ai)

### 1. Clone and install dependencies

```bash
cd LabAssistantAi
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Add your Grok API key

Edit the `.env` file:

```
XAI_API_KEY=xai-your-actual-key-here
```

### 3. Run the app

```bash
source venv/bin/activate
uvicorn main:app --reload --port 8000
```

### 4. Open in browser

Go to [http://localhost:8000](http://localhost:8000)

> The first run downloads the embedding model (~80MB) and indexes the knowledge base into ChromaDB. Subsequent starts load from disk instantly.

## Configuration

Edit `config.py` to change:

- `MODEL_NAME` — switch between Grok models (e.g., `grok-3-mini`, `grok-2`)
- `CHUNK_SIZE` / `CHUNK_OVERLAP` — tune document chunking
- `SYSTEM_PROMPT` — customize the assistant's behavior

To update the knowledge base, edit `knowledge_base/lab_manual.md` and restart the server. The vector store rebuilds automatically when the document changes.
