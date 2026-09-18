# Changelog

## [0.7.0] - 2026-09-18

### Added

- request ID generation and propagation
- request duration response headers
- structured JSON application logging
- sensitive-key redaction helper
- request latency and error metrics
- admin runtime metrics endpoint
- provider retry policy with exponential backoff
- transient Jina retry handling
- transient Groq retry handling
- provider configuration health endpoint
- application readiness endpoint
- observability and reliability documentation
- reliability unit tests

### Changed

- Jina provider calls now use bounded retries for transient failures
- Groq provider calls now use bounded retries for transient failures
- Uvicorn access logging is replaced by application request logs

### Reliability

- retryable provider failures include timeout, connection, HTTP 408, 425, 429, and 5xx conditions
- slow requests are logged at warning level
- unhandled exceptions return a generic internal error response

## [0.6.0] - 2026-09-18

### Added

- admin workflows
- operational visibility
- administrator authorization

## [0.5.0] - 2026-09-18

### Added

- authentication
- user ownership
- JWT access tokens

## [0.4.0] - 2026-09-18

### Added

- grounded RAG
- Groq answers
- citations

## [0.3.1] - 2026-09-18

### Added

- Jina embeddings
- semantic retrieval

## [0.2.1] - 2026-09-18

### Added

- document ingestion

## [0.1.0] - 2026-09-17

### Added

- FastAPI foundation
- PostgreSQL
- Docker
