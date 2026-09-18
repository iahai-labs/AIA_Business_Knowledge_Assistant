# Changelog

## [0.8.0] - 2026-09-18

### Added

- Alembic migration infrastructure
- production startup configuration validation
- MIME-type upload validation
- request body size limits
- in-memory API rate limiting
- explicit CORS policy
- trusted-host validation
- security headers middleware
- optional HSTS
- non-root Docker execution
- dropped Linux capabilities
- container health check
- security-hardening documentation
- rate-limit tests
- startup validation tests
- MIME validation tests

### Changed

- Docker image now runs as an unprivileged user
- future schema changes should use Alembic
- application startup validates production security settings

### Security

- basic abuse resistance through bounded request rates
- stricter upload validation
- safer browser-facing response headers
- stricter production environment validation

## [0.7.0] - 2026-09-18

### Added

- observability
- request IDs
- structured logging
- provider retry handling
- readiness checks

## [0.6.0] - 2026-09-18

### Added

- admin workflows
- operational visibility

## [0.5.0] - 2026-09-18

### Added

- authentication
- user ownership

## [0.4.0] - 2026-09-18

### Added

- grounded RAG
- Groq answer generation
- source citations

## [0.3.1] - 2026-09-18

### Added

- Jina embeddings
- pgvector semantic retrieval

## [0.2.1] - 2026-09-18

### Added

- document ingestion

## [0.1.0] - 2026-09-17

### Added

- FastAPI foundation
- PostgreSQL
- Docker
