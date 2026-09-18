# Architecture Decisions

## ADR-001 — Separate Embedding and Chat Providers

The system intentionally does not require a single vendor for all AI capabilities.

Jina handles vector embeddings and semantic retrieval. A separate LLM provider can handle grounded answer generation in later releases.

## ADR-002 — Jina v5 Text Small

`jina-embeddings-v5-text-small` is used for text retrieval. The project uses separate retrieval tasks for indexed passages and user queries.

## ADR-003 — 1024 Vector Dimensions

The release uses the model's 1024-dimensional output to preserve retrieval quality while keeping configuration straightforward.

## ADR-004 — Direct HTTP Client

The Jina API is called directly using HTTPX. This keeps provider behavior explicit and avoids pretending that all embedding providers are fully OpenAI-compatible.

## ADR-005 — No Alembic Yet

This portfolio milestone uses a controlled development migration for the empty chunk table. Formal schema migrations will be added before the production release.
