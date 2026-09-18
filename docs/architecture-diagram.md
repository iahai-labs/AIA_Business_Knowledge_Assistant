# Architecture Diagram

```mermaid
flowchart TD
    U[Authenticated User] --> API[FastAPI API]
    A[Administrator] --> API

    API --> SEC[Security Middleware]
    SEC --> AUTH[JWT Authentication]
    AUTH --> OWN[Ownership Boundary]

    OWN --> DOC[Document Ingestion]
    DOC --> EXT[Text Extraction]
    EXT --> CHUNK[Chunking]
    CHUNK --> JINA[Jina Embeddings]
    JINA --> PG[(PostgreSQL + pgvector)]

    OWN --> QUERY[User Query]
    QUERY --> JQ[Jina Query Embedding]
    JQ --> PG
    PG --> RET[Top-K Retrieval]
    RET --> FILTER[Similarity Filter]
    FILTER --> CTX[Context Builder]
    CTX --> GROQ[Groq LLM]
    GROQ --> ANSWER[Grounded Answer + Sources]

    API --> ADMIN[Admin Read-only APIs]
    API --> OBS[Observability]
    OBS --> LOGS[Structured Logs]
    OBS --> METRICS[Runtime Metrics]
```

## Design Principles

- one application service
- explicit provider boundaries
- user-scoped data access
- deterministic source metadata
- graceful provider failure handling
- security controls before public deployment
