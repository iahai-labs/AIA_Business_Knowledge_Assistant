# Portfolio Story

## Problem

Small and medium businesses often keep important operational knowledge in scattered PDF, TXT, and Markdown files. Employees repeatedly search documents or ask the same questions.

## Solution

AIA Business Knowledge Assistant converts business documents into a private, searchable knowledge system.

Users can:

1. upload business documents
2. index them into pgvector
3. search semantically
4. ask natural-language questions
5. receive grounded answers with source metadata
6. keep conversations separated by authenticated user

## Engineering Highlights

- FastAPI service architecture
- PostgreSQL + pgvector
- Jina embeddings
- Groq answer generation
- JWT authentication
- per-user resource isolation
- admin operational visibility
- structured logging and request tracing
- provider retries and timeouts
- rate limiting and browser security headers
- Alembic migration baseline
- Docker non-root execution

## What This Demonstrates

The project is intentionally more than a chatbot demo. It demonstrates AI integration, backend engineering, data isolation, infrastructure awareness, observability, security, and production-oriented decision making.
