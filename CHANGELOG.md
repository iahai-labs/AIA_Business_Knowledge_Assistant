# Changelog

## [0.6.0] - 2026-09-18

### Added

- administrator flag on users
- administrator authorization dependency
- read-only admin API
- system aggregate statistics
- admin user overview with document/conversation counts
- admin document overview with owner and chunk counts
- admin conversation overview with owner and message counts
- v0.5.0 to v0.6.0 database migration
- admin authorization tests
- admin response safety test
- admin workflow documentation

### Security

- admin status is checked server-side from the current database user
- non-admin authenticated users receive HTTP 403
- admin user responses never expose password hashes
- admin endpoints are read-only in this release

## [0.5.0] - 2026-09-18

### Added

- authentication
- Argon2 password hashing
- JWT access tokens
- user-owned documents
- user-owned conversations
- user-scoped retrieval

## [0.4.0] - 2026-09-18

### Added

- Groq grounded answer generation
- similarity threshold
- source citations
- conversation persistence

## [0.3.1] - 2026-09-18

### Changed

- Jina embeddings
- pgvector semantic retrieval

## [0.2.1] - 2026-09-18

### Fixed

- model registration
- release version mismatch

## [0.1.0] - 2026-09-17

### Added

- FastAPI foundation
- PostgreSQL
- Docker
- health checks
