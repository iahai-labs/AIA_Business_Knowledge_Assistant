# Observability and Reliability

## Request Correlation

Every HTTP request receives a request ID.

Clients may provide:

```text
X-Request-ID
```

If absent, the application generates one.

Responses include:

```text
X-Request-ID
X-Process-Time-Ms
```

The request ID is also included in structured logs.

## Structured Logging

By default, logs are JSON and contain:

- timestamp
- severity
- logger
- event
- request ID
- HTTP method
- request path
- status code
- duration
- provider
- operation
- retry attempt
- error type

Known sensitive keys are redacted.

## Runtime Metrics

Administrators can inspect lightweight in-process metrics:

```text
GET /api/admin/metrics
```

Metrics include:

- requests total
- server errors total
- slow requests total
- average request latency

These metrics are process-local and are intentionally lightweight. A future production deployment may export metrics to a dedicated monitoring system.

## Provider Reliability

Jina and Groq requests use bounded retry behavior for transient failures.

Retryable cases include:

- timeouts
- connection failures
- HTTP 408
- HTTP 425
- HTTP 429
- HTTP 5xx gateway/server failures

Retries use exponential backoff and are configurable.

## Health Endpoints

```text
GET /health
GET /health/db
GET /health/providers
GET /ready
```

`/health/providers` reports whether provider credentials are configured. It does not consume external API credits.

`/ready` verifies database reachability and required provider/JWT configuration.
