# AIA Business Knowledge Assistant

A production-minded AI knowledge system for small and medium businesses.

## Current Release

**v0.4.0 — Grounded Answers + Citations**

The project now provides an end-to-end Retrieval-Augmented Generation workflow.

## AI Architecture

```text
Documents
   |
   v
Jina Embeddings
   |
   v
PostgreSQL + pgvector
   |
   v
Semantic Retrieval
   |
   v
Similarity Threshold
   |
   v
Grounded Context
   |
   v
Groq LLM
   |
   v
Answer + Source Citations
```

## Current Capabilities

- PDF, TXT, and Markdown ingestion
- text extraction
- document chunking
- Jina passage/query embeddings
- pgvector semantic search
- configurable minimum similarity threshold
- Groq grounded answer generation
- inline source markers such as `[1]`
- structured source metadata
- safe no-context response
- conversation persistence
- conversation-history API
- Docker development environment
- automated tests

## Environment

Keep your v0.3.1 settings and add:

```env
APP_VERSION=0.4.0

RETRIEVAL_MIN_SIMILARITY=0.25

GROQ_API_KEY=your-key
GROQ_BASE_URL=https://api.groq.com/openai/v1
GROQ_MODEL=llama-3.1-8b-instant
GROQ_TIMEOUT_SECONDS=45
ANSWER_TEMPERATURE=0.1
MAX_CONTEXT_CHUNKS=5
```

Never commit `.env`.

## Main API

```text
POST    /api/documents
GET     /api/documents
GET     /api/documents/{document_id}
POST    /api/documents/{document_id}/index
DELETE  /api/documents/{document_id}

POST    /api/retrieval/search

POST    /api/chat/ask
GET     /api/chat/conversations/{conversation_id}
```

## Ask the Knowledge Base

```json
{
  "question": "Can this company help automate business tasks?",
  "top_k": 5
}
```

Example response shape:

```json
{
  "conversation_id": 1,
  "question": "Can this company help automate business tasks?",
  "answer": "Yes. The company provides AI automation services [1].",
  "sources": [
    {
      "reference": 1,
      "document_id": 2,
      "original_filename": "sample.txt",
      "chunk_index": 0,
      "similarity": 0.45
    }
  ],
  "grounded": true,
  "llm_provider": "groq",
  "llm_model": "llama-3.1-8b-instant"
}
```

## Safety Behavior

If no indexed chunk meets the configured similarity threshold, the application does not ask the LLM to guess. It returns:

```text
I don't have enough information in the indexed documents to answer that.
```

## Swagger

```text
http://localhost:8000/docs
```

## Tests

```powershell
docker compose exec app pytest
```

## Roadmap

- `v0.1.0` Foundation
- `v0.2.1` Document ingestion
- `v0.3.1` Jina embeddings + pgvector
- `v0.4.0` Grounded answers + citations
- `v0.5.0` Authentication and user ownership
- `v0.6.0` Admin workflows
- `v0.9.0` Release candidate
- `v1.0.0` Portfolio release

## License

MIT
