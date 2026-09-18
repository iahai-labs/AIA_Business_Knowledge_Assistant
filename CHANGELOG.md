# Changelog

## [0.4.0] - 2026-09-18

### Added

- Groq grounded answer generation
- configurable retrieval similarity threshold
- safe no-context response
- structured source citations
- inline citation prompting
- conversation model
- message model
- conversation-history endpoint
- retrieval threshold tests
- Groq client tests
- v0.4.0 upgrade guide

### Changed

- semantic retrieval can now filter low-similarity chunks
- retrieval responses expose the effective similarity threshold

## [0.3.1] - 2026-09-18

### Changed

- replaced OpenAI embeddings with Jina embeddings
- changed vector dimensions to 1024
- separated passage and query embedding tasks

## [0.2.1] - 2026-09-18

### Fixed

- SQLAlchemy circular import
- model registration
- release version mismatch

## [0.1.0] - 2026-09-17

### Added

- FastAPI foundation
- PostgreSQL
- Docker
- health checks
