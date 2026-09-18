# Changelog

## [0.3.1] - 2026-09-18

### Changed

- replaced OpenAI embedding calls with direct Jina Embeddings API integration
- changed vector dimensions from 1536 to 1024
- separated passage and query embedding tasks
- removed the OpenAI package dependency from the retrieval milestone
- improved embedding-provider error reporting

### Added

- embedding-provider configuration
- Jina embedding service tests
- v0.3.1 vector-table upgrade guide
- provider and model metadata in indexing and retrieval responses

## [0.3.0] - 2026-09-18

### Added

- pgvector-backed chunk model
- text chunking
- embedding pipeline
- semantic retrieval

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
