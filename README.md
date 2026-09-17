# AIA Business Knowledge Assistant

A production-minded AI knowledge system for small and medium businesses.

## Business Problem

Business information is often scattered across PDF files, internal guides, policies, product documents, and support material. Employees and customers waste time searching for reliable answers, and generic AI assistants may produce responses that are not grounded in the company's actual knowledge.

## Solution

AIA Business Knowledge Assistant will turn business documents into a searchable knowledge system that can answer questions using retrieved source material and provide source references for each grounded answer.

## Current Release

**v0.1.0 — Foundation**

This release provides:

- FastAPI backend
- centralized configuration
- PostgreSQL connectivity
- pgvector-ready database
- Docker Compose development environment
- health endpoints
- automated test baseline
- project documentation

## Planned Capabilities

- document upload
- file validation
- text extraction
- chunking
- embeddings
- vector retrieval
- grounded AI answers
- source citations
- conversation history
- authentication
- admin workflows
- deployment behind Nginx

## Tech Stack

- Python 3.12
- FastAPI
- SQLAlchemy 2
- PostgreSQL
- pgvector
- Docker
- Docker Compose
- pytest

## Quick Start

### 1. Create environment file

```bash
cp .env.example .env
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

### 2. Start the project

```bash
docker compose up --build
```

### 3. Check health

Open:

```text
http://localhost:8000/health
```

Expected response:

```json
{
  "status": "ok",
  "service": "AIA Business Knowledge Assistant",
  "version": "0.1.0"
}
```

### 4. Check database health

```text
http://localhost:8000/health/db
```

### 5. Run tests

```bash
docker compose exec app pytest
```

## Security Baseline

- secrets are loaded from environment variables
- `.env` is ignored by Git
- production debug mode must be disabled
- no API key should ever be committed
- database credentials must be replaced before deployment

## Roadmap

- `v0.1.0` Foundation
- `v0.2.0` Document ingestion
- `v0.3.0` RAG retrieval
- `v0.4.0` Chat and citations
- `v0.5.0` Authentication
- `v0.6.0` Admin workflows
- `v0.9.0` Release candidate
- `v1.0.0` Portfolio release

## License

MIT
