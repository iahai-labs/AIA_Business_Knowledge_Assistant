# Architecture

## Current Scope

Version 0.1.0 establishes the project foundation:

- FastAPI application
- Central configuration
- PostgreSQL connectivity
- Docker development environment
- Health endpoints
- Automated test baseline

## High-Level Architecture

```text
Browser / API Client
        |
        v
     FastAPI
        |
        +--> API Routes
        |
        +--> Services (future)
        |
        +--> Repository Layer (future)
        |
        v
   PostgreSQL + pgvector
```

## Future Layers

Later releases will introduce:

- document ingestion
- text extraction
- chunking
- embeddings
- vector retrieval
- grounded answer generation
- source citations
- authentication
- admin workflows
