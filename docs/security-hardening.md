# Security and Production Hardening

## v0.8.0 Controls

### HTTP Security Headers

Responses include:

- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `Referrer-Policy: no-referrer`
- restrictive `Permissions-Policy`
- restrictive `Content-Security-Policy`
- optional HSTS

### Rate Limiting

A lightweight in-memory rate limiter protects API endpoints from basic abuse.

Health and readiness endpoints are excluded.

This is sufficient for a single-process portfolio deployment. A horizontally scaled production deployment should use a shared limiter backed by infrastructure such as Redis or an API gateway.

### Request Size Limit

Requests exceeding the configured `MAX_REQUEST_BODY_MB` are rejected with HTTP 413.

### Upload Validation

Uploads are checked by:

- extension allowlist
- MIME-type allowlist
- file-size limit
- duplicate SHA-256 detection

### Startup Validation

Production and staging startup fails when critical security configuration is missing or obviously unsafe.

### Docker Hardening

The application image:

- runs as a non-root user
- drops Linux capabilities
- enables `no-new-privileges`
- exposes a container health check

### Database Migrations

Alembic becomes the migration source of truth from v0.8.0 onward.

Older manual migration scripts remain as project history but should not be used for future schema evolution.
