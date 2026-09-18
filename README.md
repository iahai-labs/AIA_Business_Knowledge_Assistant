# AIA Business Knowledge Assistant

A production-minded, multi-user RAG knowledge system for small and medium businesses.

## Current Release

**v0.7.0 — Observability + Reliability**

This release adds request tracing, structured logging, provider retries, readiness checks, and lightweight runtime metrics.

## Architecture

```text
Authenticated User
      |
      v
FastAPI
      |
      +--> Request ID + Timing
      |
      +--> User-owned RAG
      |       |
      |       +--> Jina Embeddings
      |       +--> pgvector
      |       +--> Groq Grounded Answers
      |
      +--> Admin Workflows
      |
      v
Structured Logs + Runtime Metrics
```

## Current Capabilities

- email/password authentication
- Argon2 password hashing
- JWT bearer authentication
- per-user document ownership
- per-user retrieval isolation
- Jina embeddings
- PostgreSQL + pgvector
- Groq grounded answers
- source metadata
- safe no-context behavior
- conversation persistence
- read-only admin workflows
- request IDs
- request latency headers
- JSON structured logging
- sensitive-key redaction
- bounded provider retries
- provider timeout handling
- database health check
- provider configuration health
- readiness endpoint
- admin runtime metrics
- automated reliability tests

## Health and Readiness

```text
GET /health
GET /health/db
GET /health/providers
GET /ready
```

## Runtime Metrics

Admin-only:

```text
GET /api/admin/metrics
```

## Request Diagnostics

Responses include:

```text
X-Request-ID
X-Process-Time-Ms
```

Use the request ID to correlate client failures with application logs.

## Logs

```powershell
docker compose logs app -f
```

## Upgrade

Read:

```text
docs/upgrade-v0.7.0.md
```

No database schema migration is required for this release.

## Tests

```powershell
docker compose exec app pytest
```

## Roadmap

- `v0.1.0` Foundation
- `v0.2.1` Document ingestion
- `v0.3.1` Jina embeddings + pgvector
- `v0.4.0` Grounded answers + citations
- `v0.5.0` Authentication + user ownership
- `v0.6.0` Admin workflows + operational visibility
- `v0.7.0` Observability + reliability
- `v0.8.0` Security + production hardening
- `v0.9.0` Release candidate
- `v1.0.0` Portfolio release

## License

MIT
