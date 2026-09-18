# AIA Business Knowledge Assistant

A production-minded AI knowledge system for small and medium businesses.

## Current Release

**v0.6.0 — Admin Workflows + Operational Visibility**

The system now combines multi-user RAG with a minimal read-only administrator layer.

## Architecture

```text
Users
  |
  +--> JWT-authenticated user APIs
  |       |
  |       +--> owned documents
  |       +--> Jina embeddings
  |       +--> pgvector retrieval
  |       +--> Groq grounded answers
  |       +--> owned conversations
  |
  +--> Admin authorization
          |
          +--> system stats
          +--> user overview
          +--> document overview
          +--> conversation overview
```

## Current Capabilities

- email/password registration
- Argon2 password hashing
- JWT bearer authentication
- per-user document ownership
- per-user vector retrieval
- per-user conversation isolation
- Jina embeddings
- PostgreSQL + pgvector
- Groq grounded answers
- source metadata
- safe no-context responses
- read-only admin authorization
- system operational statistics
- admin user overview
- admin document overview
- admin conversation overview
- automated security and authorization tests

## Admin API

```text
GET /api/admin/stats
GET /api/admin/users
GET /api/admin/documents
GET /api/admin/conversations
```

Admin endpoints require a user whose database record has:

```text
is_admin = TRUE
```

Normal authenticated users receive HTTP 403.

## Upgrade

Read:

```text
docs/upgrade-v0.6.0.md
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
- `v0.5.0` Authentication + user ownership
- `v0.6.0` Admin workflows + operational visibility
- `v0.9.0` Release candidate
- `v1.0.0` Portfolio release

## License

MIT
