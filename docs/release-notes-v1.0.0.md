# AIA Business Knowledge Assistant v1.0.0

## Final Portfolio Release

Version 1.0.0 marks the first stable portfolio release.

The project demonstrates a production-minded Retrieval-Augmented Generation system with multi-user isolation, operational visibility, security controls, and deployment documentation.

## Core Capabilities

- business document ingestion
- PDF, TXT, and Markdown support
- chunking and embeddings
- PostgreSQL + pgvector semantic retrieval
- Jina embeddings
- Groq grounded answer generation
- source metadata and safe no-context fallback
- conversation persistence
- email/password authentication
- Argon2 password hashing
- JWT access tokens
- per-user document and conversation ownership
- read-only administrator workflows
- structured JSON logging
- request IDs and timing
- provider retries and timeouts
- health and readiness endpoints
- runtime metrics
- rate limiting
- request-size limits
- MIME validation
- CORS and trusted-host policies
- security headers
- non-root Docker execution
- Alembic migration baseline

## Final Release Checks

Before publishing:

```powershell
docker compose exec app pytest
docker compose exec app python scripts/smoke_test.py
docker compose exec app alembic current
```

Expected Alembic revision:

```text
0001 (head)
```

## Demo Scenario

Upload:

```text
demo_data/automation_services.txt
```

Ask:

```text
Can the company automate repetitive business tasks?
```

Then demonstrate safe fallback with:

```text
What is the weather in Berlin today?
```

## Known Scope Boundaries

This release intentionally does not include:

- OAuth or social login
- MFA
- organization/team RBAC
- refresh-token rotation
- distributed rate limiting
- multi-region deployment
- billing
- background job queues
- advanced reranking

These are outside the portfolio v1 scope.
