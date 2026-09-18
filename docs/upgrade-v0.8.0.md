# Upgrade to v0.8.0

## 1. Update `.env`

Set:

```env
APP_VERSION=0.8.0

ALLOWED_MIME_TYPES=application/pdf,text/plain,text/markdown

CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
RATE_LIMIT_REQUESTS=60
RATE_LIMIT_WINDOW_SECONDS=60
MAX_REQUEST_BODY_MB=12
TRUSTED_HOSTS=localhost,127.0.0.1
ENABLE_HSTS=false
```

Keep all existing database, Jina, Groq, JWT, and observability settings.

## 2. Rebuild

```powershell
docker compose down
docker compose build --no-cache
docker compose up -d
```

## 3. Establish Alembic baseline

v0.8.0 introduces Alembic for future schema migrations.

Because the current database already has the schema created by earlier releases, stamp the baseline without replaying old schema changes:

```powershell
docker compose exec app alembic stamp 0001
```

Verify:

```powershell
docker compose exec app alembic current
```

Expected:

```text
0001 (head)
```

Future schema changes should use:

```powershell
docker compose exec app alembic upgrade head
```

## 4. Tests

```powershell
docker compose exec app pytest
```

## 5. Security Checks

Verify response headers:

```text
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Referrer-Policy: no-referrer
```

Verify normal requests work and excessive repeated requests eventually receive:

```text
429 Too Many Requests
```

## 6. Production Notes

For production:

```env
ENVIRONMENT=production
DEBUG=false
ENABLE_HSTS=true
TRUSTED_HOSTS=your-domain.example.com
CORS_ALLOWED_ORIGINS=https://your-frontend.example.com
```

Do not use wildcard trusted hosts or wildcard CORS origins in production.
