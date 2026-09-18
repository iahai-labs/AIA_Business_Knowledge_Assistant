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


## Administrator Access

Administrator privileges are stored as a server-side boolean on the user record.

The API does not trust a client-supplied role or JWT claim for administrator status. It loads the current user from the database and checks `is_admin` on each protected admin request.

Admin endpoints are read-only in v0.6.0 and do not expose password hashes or application secrets.


## Privacy-Conscious Logging

Observability logs must not intentionally include passwords, access tokens, API keys, JWT secrets, or password hashes.

Known sensitive dictionary keys are redacted by the logging helper. Application code should still avoid logging raw request bodies and credentials.


## v0.8.0 Hardening

Additional controls now include MIME validation, request-size limits, trusted-host enforcement, explicit CORS configuration, rate limiting, security headers, production startup validation, and non-root Docker execution.

Future production deployments should move rate limiting to shared infrastructure when more than one application process is used.
