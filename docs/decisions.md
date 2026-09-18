# Architecture Decisions

## ADR-001 — FastAPI

FastAPI remains the backend framework.

## ADR-002 — PostgreSQL + pgvector

PostgreSQL remains the primary data store. Vector support will be activated in the RAG milestone.

## ADR-003 — Local Storage for Portfolio Demo

Uploaded files are stored on local disk for the portfolio demo. This keeps the deployment simple while preserving a clear abstraction boundary for future object storage.

For a larger production deployment, this can be replaced with S3-compatible object storage.

## ADR-004 — SHA-256 Duplicate Detection

The ingestion pipeline hashes file contents and rejects duplicate documents.

## ADR-005 — Allowlist File Validation

Version 0.2.0 accepts PDF, TXT, and Markdown files only. Additional formats must be explicitly introduced with their own text extractors and validation rules.
