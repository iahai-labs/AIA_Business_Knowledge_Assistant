# Upgrade to v0.6.0

## 1. Update version

Set:

```env
APP_VERSION=0.6.0
```

Keep the existing Jina, Groq, database, and JWT settings.

## 2. Stop the application

```powershell
docker compose down
```

## 3. Start PostgreSQL

```powershell
docker compose up -d db
```

## 4. Apply the migration

```powershell
Get-Content scripts/migrate_v050_to_v060.sql | docker compose exec -T db psql -U aia -d aia_knowledge
```

Expected final line:

```text
COMMIT
```

## 5. Promote one existing user to administrator

Replace the example email:

```powershell
docker compose exec db psql -U aia -d aia_knowledge -c "UPDATE users SET is_admin = TRUE WHERE email = 'demo@example.com';"
```

Verify:

```powershell
docker compose exec db psql -U aia -d aia_knowledge -c "SELECT id, email, is_active, is_admin FROM users ORDER BY id;"
```

## 6. Rebuild and start

```powershell
docker compose down
docker compose build --no-cache
docker compose up -d
```

## 7. Test

```powershell
docker compose exec app pytest
```

## 8. Login again

Existing JWT tokens do not include the admin flag, but the API checks the current database user on each request. Logging in again is still recommended for a clean manual test session.

## 9. Admin API

Authenticate in Swagger and test:

```text
GET /api/admin/stats
GET /api/admin/users
GET /api/admin/documents
GET /api/admin/conversations
```

A normal user should receive HTTP 403 for these endpoints.
