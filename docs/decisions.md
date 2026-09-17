# Architecture Decisions

## ADR-001 — FastAPI

FastAPI is used as the backend framework because the project is API-oriented, Python-based, and expected to integrate AI and document-processing services.

## ADR-002 — PostgreSQL + pgvector

PostgreSQL is the primary relational database. The pgvector extension will be used for vector similarity search so structured business data and vector data can remain in the same database for the first production-ready iteration.

## ADR-003 — Server-rendered UI First

The first portfolio release will prefer a lightweight server-rendered interface before considering a separate frontend framework.

## ADR-004 — Monolith First

The project starts as a modular monolith. Microservices are intentionally deferred until there is a real operational need.
