# AIA Business Knowledge Assistant

A production-minded AI knowledge system for small and medium businesses.

## Current Release

**v0.3.1 — Jina Embeddings + pgvector**

This release uses a dedicated retrieval provider rather than coupling embeddings to the future chat model.

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

Future v0.4:
Retrieved Context
   |
   v
Groq LLM
   |
   v
Grounded Answer + Sources
```

## Current Capabilities

- PDF, TXT, and Markdown ingestion
- text extraction
- configurable chunking
- Jina text embeddings
- separate `retrieval.passage` and `retrieval.query` tasks
- 1024-dimensional pgvector storage
- semantic similarity search
- top-k retrieval
- source document metadata
- duplicate-file detection
- Docker development environment
- automated tests

## Jina Configuration

Create a free Jina API key and configure:

```env
EMBEDDING_PROVIDER=jina
JINA_API_KEY=your-key
JINA_BASE_URL=https://api.jina.ai/v1
EMBEDDING_MODEL=jina-embeddings-v5-text-small
EMBEDDING_DIMENSIONS=1024
```

Do not commit `.env`.

## Upgrade from v0.3.0

Read:

```text
docs/upgrade-v0.3.1.md
```

The vector dimension changed from 1536 to 1024, so an existing empty `document_chunks` table from v0.3.0 must be recreated.

## Main API

```text
POST    /api/documents
GET     /api/documents
GET     /api/documents/{document_id}
POST    /api/documents/{document_id}/index
DELETE  /api/documents/{document_id}

POST    /api/retrieval/search
```

Swagger:

```text
http://localhost:8000/docs
```

## Example Retrieval Request

```json
{
  "query": "What services does the company provide?",
  "top_k": 5
}
```

## Tests

```powershell
docker compose exec app pytest
```

## Roadmap

- `v0.1.0` Foundation
- `v0.2.1` Document ingestion
- `v0.3.1` Jina embeddings + pgvector
- `v0.4.0` Groq grounded answers + citations
- `v0.5.0` Authentication
- `v0.6.0` Admin workflows
- `v0.9.0` Release candidate
- `v1.0.0` Portfolio release

## License

MIT
