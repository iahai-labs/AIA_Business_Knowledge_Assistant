# AIA Business Knowledge Assistant

A production-minded, multi-user RAG knowledge system for small and medium businesses.

## Current Release

**v0.8.0 — Security + Production Hardening**

This release adds application security controls, Docker hardening, startup validation, and Alembic migration management.

## Architecture

```text
Client
  |
  v
Security Middleware
  |
  +--> Trusted Hosts
  +--> CORS
  +--> Request Size Limit
  +--> Rate Limit
  +--> Security Headers
  +--> Request Tracing
  |
  v
FastAPI
  |
  +--> Auth + Ownership
  +--> Jina + pgvector
  +--> Groq Grounded RAG
  +--> Admin Workflows
  |
  v
Structured Logs + Runtime Metrics
```

## Security Controls

- Argon2 password hashing
- JWT authentication
- user ownership isolation
- admin authorization
- upload extension validation
- MIME allowlist
- request body size limit
- rate limiting
- explicit CORS policy
- trusted-host validation
- security headers
- optional HSTS
- production startup validation
- privacy-conscious logs
- non-root Docker user
- dropped Linux capabilities
- container health check

## Database Migrations

Alembic is now the migration source of truth.

For an existing v0.7.0 database:

```powershell
docker compose exec app alembic stamp 0001
```

Future releases:

```powershell
docker compose exec app alembic upgrade head
```

## Upgrade

Read:

```text
docs/upgrade-v0.8.0.md
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
- `v0.5.0` Authentication + user ownership
- `v0.6.0` Admin workflows + operational visibility
- `v0.7.0` Observability + reliability
- `v0.8.0` Security + production hardening
- `v0.9.0` Release candidate
- `v1.0.0` Portfolio release

## License

MIT
