# Upgrade to v0.9.0

## Database

No schema migration is required.

Verify Alembic:

```powershell
docker compose exec app alembic current
```

Expected baseline:

```text
0001 (head)
```

## Environment

Set:

```env
APP_VERSION=0.9.0
```

Keep all v0.8.0 security, provider, database, JWT, and observability settings.

## Rebuild

```powershell
docker compose down
docker compose build --no-cache
docker compose up -d
```

## Tests

```powershell
docker compose exec app pytest
```

## Smoke Test

```powershell
docker compose exec app python scripts/smoke_test.py
```

## Manual Release Candidate Verification

Verify:

```text
GET /health
GET /health/db
GET /health/providers
GET /ready
GET /release
```

Then test:

- registration
- login
- authentication
- upload
- indexing
- semantic retrieval
- grounded chat
- negative/no-context chat
- conversation history
- admin endpoints
- non-admin 403 behavior
- rate limiting
- security headers

## Release Candidate Rule

Do not add new product features after v0.9.0 unless they fix a release-blocking defect.

The remaining work should be documentation, demo polish, bug fixes, deployment verification, and final portfolio presentation.
