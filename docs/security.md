# Security Notes

## Passwords

Passwords are hashed using Argon2 through `argon2-cffi`.

The API never returns password hashes.

## JWT

Access tokens contain:

- `sub`: user ID
- `iat`: issued-at timestamp
- `exp`: expiration timestamp
- `type`: access

Generate a strong random `JWT_SECRET_KEY`. Do not commit it.

Example PowerShell command:

```powershell
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

## Resource Isolation

Every protected data access path includes the current authenticated user's ID.

A user requesting another user's document or conversation receives a not-found response rather than resource details.

## Current Limitations

v0.5.0 intentionally does not yet include:

- refresh tokens
- email verification
- password reset
- MFA
- organization/team roles
- OAuth/SSO
- rate limiting

Those belong to later hardening milestones.
