# Deployment Guide

## Target

This guide describes a simple single-server deployment using Docker Compose and a reverse proxy.

## Production Environment

Use values similar to:

```env
APP_VERSION=0.9.0
ENVIRONMENT=production
DEBUG=false

ENABLE_HSTS=true
TRUSTED_HOSTS=knowledge.example.com
CORS_ALLOWED_ORIGINS=https://knowledge.example.com
```

Provide strong secrets for:

```text
JWT_SECRET_KEY
JINA_API_KEY
GROQ_API_KEY
```

Do not commit `.env`.

## Database

Use PostgreSQL with pgvector enabled.

For an existing v0.8.0 database:

```bash
alembic upgrade head
```

For the current baseline, verify:

```bash
alembic current
```

## Reverse Proxy

Terminate TLS at Nginx, Caddy, Traefik, or another trusted reverse proxy.

Forward requests to:

```text
127.0.0.1:8000
```

Forward the original host and request ID headers.

## Container Checks

After deployment:

```bash
docker compose ps
docker compose logs app --tail 100
```

Then verify:

```text
GET /health
GET /health/db
GET /health/providers
GET /ready
GET /release
```

## Production Notes

The built-in rate limiter is process-local. Multi-instance deployments should move rate limiting to shared infrastructure such as Redis or an API gateway.

The current application is designed as a portfolio-grade single-service architecture, not a multi-region platform.
