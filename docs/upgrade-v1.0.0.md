# Upgrade to v1.0.0

## Database

No schema migration is required from v0.9.0.

Verify:

```powershell
docker compose exec app alembic current
```

Expected:

```text
0001 (head)
```

## Environment

Set:

```env
APP_VERSION=1.0.0
```

For local development:

```env
ENVIRONMENT=development
DEBUG=true
TRUSTED_HOSTS=localhost,127.0.0.1,testserver
ENABLE_HSTS=false
```

For production, replace trusted hosts and CORS origins with the real domain and use:

```env
ENVIRONMENT=production
DEBUG=false
ENABLE_HSTS=true
```

## Rebuild

```powershell
docker compose down
docker compose build --no-cache
docker compose up -d
```

## Final Validation

```powershell
docker compose exec app pytest
docker compose exec app python scripts/smoke_test.py
docker compose exec app alembic current
```

Then run the manual demo flow described in `docs/demo-script.md`.
