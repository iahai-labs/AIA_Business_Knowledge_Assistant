# AIA Business Knowledge Assistant

A production-minded AI knowledge system for small and medium businesses.

## Current Release

**v0.5.0 — Authentication + User Ownership**

The application now isolates documents, retrieval, and conversations by authenticated user.

## Architecture

```text
User
  |
  v
Register / Login
  |
  v
Argon2 + JWT
  |
  v
Authenticated API
  |
  +--> User Documents
  |       |
  |       v
  |    Jina Embeddings
  |       |
  |       v
  |    pgvector Retrieval
  |
  +--> User Conversations
          |
          v
       Groq Grounded Answers
```

## Current Capabilities

- email/password registration
- Argon2 password hashing
- JWT bearer authentication
- current-user endpoint
- user-owned documents
- user-scoped semantic retrieval
- user-owned conversations
- conversation history isolation
- PDF/TXT/Markdown ingestion
- Jina embeddings
- PostgreSQL + pgvector
- similarity threshold
- Groq grounded answers
- source metadata
- safe no-context response
- automated tests

## Authentication API

```text
POST /api/auth/register
POST /api/auth/login
GET  /api/auth/me
```

## Protected API

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

## Required JWT Configuration

```env
JWT_SECRET_KEY=use-a-strong-random-secret
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_MINUTES=60
```

Generate a development secret:

```powershell
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

Never commit `.env`.

## Upgrade

Read:

```text
docs/upgrade-v0.5.0.md
```

The database requires a one-time migration because existing `documents` and `conversations` tables predate ownership fields.

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
- `v0.6.0` Admin workflows
- `v0.9.0` Release candidate
- `v1.0.0` Portfolio release

## License

MIT
