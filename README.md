# AIA Business Knowledge Assistant

A production-minded, multi-user Retrieval-Augmented Generation system for small and medium businesses.

## Release Candidate

**v0.9.0**

The project is now feature-complete for the portfolio release and is in release-candidate validation.

## What It Does

Business users upload internal documents and ask natural-language questions. The system retrieves relevant document chunks and produces grounded answers with source metadata.

```text
Business Documents
        |
        v
Text Extraction + Chunking
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
Similarity Filter
        |
        v
Groq LLM
        |
        v
Grounded Answer + Sources
```

## Engineering Features

- FastAPI
- PostgreSQL
- pgvector
- Jina embeddings
- Groq LLM integration
- PDF/TXT/Markdown ingestion
- semantic retrieval
- grounded RAG answers
- source metadata
- conversation persistence
- email/password authentication
- Argon2 password hashing
- JWT bearer authentication
- user-owned documents
- user-owned conversations
- admin read-only operations
- structured JSON logging
- request IDs
- request latency tracking
- provider retries and timeouts
- runtime metrics
- CORS policy
- trusted-host validation
- request-size limits
- rate limiting
- MIME validation
- security headers
- non-root Docker execution
- Alembic migration management

## Demo Data

Sample business documents are included in:

```text
demo_data/
```

Recommended demo flow:

1. register a user
2. log in
3. authorize in Swagger
4. upload `demo_data/automation_services.txt`
5. index the document
6. ask:

```text
Can the company automate repetitive business tasks?
```

7. ask an unrelated question to demonstrate safe fallback

## Operational Endpoints

```text
GET /health
GET /health/db
GET /health/providers
GET /ready
GET /release
```

Admin-only:

```text
GET /api/admin/stats
GET /api/admin/users
GET /api/admin/documents
GET /api/admin/conversations
GET /api/admin/metrics
```

## Development

```powershell
docker compose up --build -d
docker compose exec app pytest
```

Swagger:

```text
http://localhost:8000/docs
```

## Database Migrations

```powershell
docker compose exec app alembic current
docker compose exec app alembic upgrade head
```

## Smoke Test

```powershell
docker compose exec app python scripts/smoke_test.py
```

## Documentation

- `docs/architecture.md`
- `docs/architecture-diagram.md`
- `docs/api-examples.md`
- `docs/deployment.md`
- `docs/production-checklist.md`
- `docs/security.md`
- `docs/security-hardening.md`
- `docs/observability.md`
- `docs/portfolio-story.md`
- `docs/upgrade-v0.9.0.md`

## Roadmap

- `v0.1.0` Foundation
- `v0.2.1` Document ingestion
- `v0.3.1` Jina embeddings + semantic retrieval
- `v0.4.0` Grounded RAG + Groq + citations
- `v0.5.0` Authentication + user ownership
- `v0.6.0` Admin workflows
- `v0.7.0` Observability + reliability
- `v0.8.0` Security + production hardening
- `v0.9.0` Release candidate
- `v1.0.0` Portfolio release

## License

MIT
