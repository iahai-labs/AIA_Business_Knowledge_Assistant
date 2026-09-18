# Architecture Decisions

## ADR-001 — Jina for Embeddings

Jina remains the dedicated embedding provider.

## ADR-002 — Groq for Answer Generation

Groq is used only after retrieval has selected grounded business context.

## ADR-003 — Direct HTTP Provider Clients

Jina and Groq are called through explicit HTTPX integrations. This keeps provider contracts visible and avoids unnecessary SDK coupling.

## ADR-004 — Similarity Threshold Before Generation

Retrieved chunks below the configured threshold are excluded before calling the LLM.

## ADR-005 — Safe Empty-Context Behavior

If no chunk passes the threshold, the system does not call the LLM. It returns a deterministic insufficient-information response instead.

## ADR-006 — Minimal Conversation Persistence

Conversation history is persisted now, while authentication and user ownership are intentionally deferred to v0.5.0.
