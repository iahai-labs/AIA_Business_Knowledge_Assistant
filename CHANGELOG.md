# Changelog

## [0.5.0] - 2026-09-18

### Added

- user model
- email/password registration
- Argon2 password hashing
- JWT access tokens
- bearer authentication
- current-user endpoint
- document ownership
- conversation ownership
- user-scoped vector retrieval
- ownership-aware document access
- ownership-aware conversation history
- security documentation
- v0.4.0 to v0.5.0 SQL migration
- password and JWT tests

### Changed

- all document, retrieval, and chat endpoints now require authentication
- duplicate document detection is scoped per user
- semantic search only searches chunks owned by the authenticated user
- Groq default model set to `openai/gpt-oss-120b`

### Security

- cross-user document access returns not found
- cross-user conversation access returns not found
- plaintext passwords are never stored

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
