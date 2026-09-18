# AIA Business Knowledge Assistant

A production-minded AI knowledge system for small and medium businesses.

## Business Problem

Business information is often scattered across PDFs, internal guides, policies, product documents, and support material. Employees and customers waste time searching for reliable answers, while generic AI assistants may respond without grounding in the company's actual knowledge.

## Solution

AIA Business Knowledge Assistant turns business documents into a searchable knowledge system. The final portfolio release will answer questions using retrieved company knowledge and provide source references.

## Current Release

**v0.2.0 — Document Ingestion**

This release adds:

- document upload API
- PDF, TXT, and Markdown support
- file extension allowlist
- upload size validation
- SHA-256 duplicate detection
- server-generated storage filenames
- PDF text extraction
- document metadata persistence
- extracted text persistence
- list, detail, and delete document endpoints
- document validation tests

## API Endpoints

```text
GET     /health
GET     /health/db

POST    /api/documents
GET     /api/documents
GET     /api/documents/{document_id}
DELETE  /api/documents/{document_id}
```

Interactive API documentation is available at:

```text
http://localhost:8000/docs
```

## Tech Stack

- Python 3.12
- FastAPI
- SQLAlchemy 2
- PostgreSQL
- pgvector-ready PostgreSQL image
- PyPDF
- Docker
- Docker Compose
- pytest

## Quick Start

### 1. Create environment file

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Linux/macOS:

```bash
cp .env.example .env
```

### 2. Start the project

```bash
docker compose up --build
```

### 3. Run tests

```bash
docker compose exec app pytest
```

### 4. Upload a document

Use Swagger UI:

```text
http://localhost:8000/docs
```

Open `POST /api/documents`, choose a PDF, TXT, or Markdown file, and execute the request.

## Security Baseline

- `.env` and runtime uploads are excluded from Git
- upload extensions use an explicit allowlist
- file size is limited
- storage filenames are generated on the server
- raw user filenames are not used as paths
- duplicate content is detected using SHA-256
- API credentials should never be committed

## Repository Structure

```text
app/
  api/
  core/
  db/
  models/
  repositories/
  schemas/
  services/
docs/
tests/
uploads/          # runtime only, not committed
```

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
