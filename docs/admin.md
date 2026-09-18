# Admin Workflows

## Purpose

The v0.6.0 admin layer provides operational visibility without introducing a complex RBAC system.

## Admin Endpoints

```text
GET /api/admin/stats
GET /api/admin/users
GET /api/admin/documents
GET /api/admin/conversations
```

## System Stats

The stats endpoint exposes aggregate operational counts:

- total users
- active users
- admin users
- documents
- indexed chunks
- conversations
- messages

## Safe User View

Admin user responses intentionally exclude:

- password hashes
- JWT secrets
- provider API keys
- uploaded file contents

## Authorization

Admin access requires both:

1. a valid authenticated user
2. `users.is_admin = TRUE`

A non-admin authenticated user receives HTTP 403.

## Scope

This release is intentionally read-only for administrative operations.

It does not yet include:

- deleting users
- disabling accounts through admin API
- changing roles through API
- editing documents
- viewing raw message content in admin listings
- audit logs
- billing
