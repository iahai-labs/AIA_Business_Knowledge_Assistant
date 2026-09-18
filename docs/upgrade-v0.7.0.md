# Upgrade to v0.7.0

## Database

No schema migration is required for v0.7.0.

## Environment

Set:

```env
APP_VERSION=0.7.0

LOG_LEVEL=INFO
LOG_JSON=true

PROVIDER_RETRY_ATTEMPTS=3
PROVIDER_RETRY_BACKOFF_SECONDS=0.4
REQUEST_SLOW_THRESHOLD_MS=1500
```

Keep all existing database, Jina, Groq, and JWT settings.

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

## Manual Verification

Check:

```text
GET /health
GET /health/db
GET /health/providers
GET /ready
```

Then make any API request and inspect:

```text
X-Request-ID
X-Process-Time-Ms
```

Finally, authenticate as an admin and test:

```text
GET /api/admin/metrics
```

## Logs

Follow application logs:

```powershell
docker compose logs app -f
```

You should see structured request and provider events.
