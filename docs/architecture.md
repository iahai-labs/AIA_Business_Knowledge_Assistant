# Architecture

## Version 0.3.1 Scope

Version 0.3.1 replaces OpenAI embeddings with a dedicated Jina embedding provider while preserving PostgreSQL + pgvector retrieval.

## Retrieval Architecture

```text
Business Documents
        |
        v
Text Extraction
        |
        v
Chunking
        |
        v
Jina Embeddings API
  retrieval.passage
        |
        v
PostgreSQL + pgvector
        |
        v
User Query
        |
        v
Jina Embeddings API
  retrieval.query
        |
        v
Cosine Similarity Search
        |
        v
Top-K Relevant Chunks
```

## Provider Separation

Embedding generation is isolated behind the embedding service. The future answer-generation layer can therefore use a different LLM provider such as Groq without changing vector retrieval.

## Vector Dimension

`jina-embeddings-v5-text-small` produces 1024-dimensional embeddings by default and supports Matryoshka dimensions. This release uses 1024 dimensions.

## Upgrade Note

Version 0.3.0 used a 1536-dimensional vector column. PostgreSQL does not automatically change an existing vector column when SQLAlchemy metadata changes.

Because v0.3.0 never produced successful embeddings in this development environment, drop and recreate only the `document_chunks` table before starting v0.3.1.

The original `documents` table and uploaded-document metadata remain intact.
