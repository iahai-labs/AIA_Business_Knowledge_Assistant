# Upgrade to v0.5.0

## 1. Update `.env`

Set:

```env
APP_VERSION=0.5.0

JWT_SECRET_KEY=replace-with-a-strong-random-secret
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_MINUTES=60
```

Keep your existing Jina and Groq configuration.

Generate a local secret with:

```powershell
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

## 2. Stop the app

```powershell
docker compose down
```

## 3. Start only PostgreSQL

```powershell
docker compose up -d db
```

## 4. Apply the database migration

From PowerShell:

```powershell
Get-Content scripts/migrate_v040_to_v050.sql | docker compose exec -T db psql -U aia -d aia_knowledge
```

Expected final line:

```text
COMMIT
```

## 5. Rebuild and start

```powershell
docker compose down
docker compose build --no-cache
docker compose up -d
```

## 6. Run tests

```powershell
docker compose exec app pytest
```

## 7. Register an account

Swagger:

```text
http://localhost:8000/docs
```

Call:

```text
POST /api/auth/register
```

Example:

```json
{
  "email": "demo@example.com",
  "password": "StrongDemoPassword123!"
}
```

## 8. Login

Call:

```text
POST /api/auth/login
```

Copy the returned `access_token`.

## 9. Authenticate in Swagger

Click `Authorize` and paste the token as the bearer credential.

## 10. Recreate or reassign legacy demo content

Documents and conversations created before v0.5.0 have `owner_user_id = NULL` and are intentionally invisible.

The simplest development workflow is to upload and index a fresh demo document while authenticated.
