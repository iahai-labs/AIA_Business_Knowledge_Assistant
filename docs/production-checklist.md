# Production Checklist

## Configuration

- [ ] `ENVIRONMENT=production`
- [ ] `DEBUG=false`
- [ ] strong `JWT_SECRET_KEY`
- [ ] valid Jina API key
- [ ] valid Groq API key
- [ ] production database URL
- [ ] explicit trusted host list
- [ ] explicit CORS origin list
- [ ] HSTS enabled behind HTTPS

## Database

- [ ] PostgreSQL reachable
- [ ] pgvector extension enabled
- [ ] Alembic revision is current
- [ ] database backup strategy defined
- [ ] restore procedure tested

## Security

- [ ] `.env` excluded from Git
- [ ] non-root container confirmed
- [ ] security headers verified
- [ ] rate limiting verified
- [ ] upload limits verified
- [ ] admin endpoints require admin account
- [ ] cross-user resource isolation tested

## AI Providers

- [ ] Jina embeddings tested
- [ ] Groq generation tested
- [ ] provider timeout behavior tested
- [ ] retry behavior tested
- [ ] safe no-context response tested

## Operations

- [ ] `/health` returns 200
- [ ] `/ready` returns 200
- [ ] structured logs visible
- [ ] request IDs visible
- [ ] admin metrics endpoint tested
- [ ] container health status is healthy
