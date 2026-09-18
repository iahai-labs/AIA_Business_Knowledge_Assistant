# Architecture

## Version 0.4.0 Scope

Version 0.4.0 adds grounded answer generation, source citations, confidence filtering, and conversation persistence.

## End-to-End RAG Flow

```text
User Question
     |
     v
Jina Query Embedding
     |
     v
PostgreSQL + pgvector
     |
     v
Top-K Retrieval
     |
     v
Minimum Similarity Filter
     |
     +---- no trusted context ----> Safe "not enough information" response
     |
     v
Context Builder
     |
     v
Groq Chat Completion
     |
     v
Grounded Answer + Inline [n] Citations
     |
     v
Conversation + Message Persistence
```

## Provider Separation

- Jina: embeddings and semantic retrieval
- PostgreSQL + pgvector: vector storage and ranking
- Groq: grounded answer generation

This avoids vendor lock-in and lets each provider serve a specific role.

## Grounding Rule

The LLM receives an explicit instruction to answer only from retrieved context. It must state that there is not enough indexed information when context is insufficient.

## Similarity Threshold

Low-similarity chunks are removed before context construction. The default threshold is configurable with `RETRIEVAL_MIN_SIMILARITY`.

The threshold is a tuning parameter, not a universal confidence probability.

## Conversation Persistence

Each `/api/chat/ask` request creates a conversation when no `conversation_id` is supplied. User and assistant messages are stored in PostgreSQL.
