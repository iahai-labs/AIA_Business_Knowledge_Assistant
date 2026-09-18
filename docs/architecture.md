# Architecture

## Version 0.5.0 Scope

Version 0.5.0 adds authentication and user ownership to the existing RAG system.

## Authentication Flow

```text
Register
   |
   v
Argon2 Password Hash
   |
   v
User Record

Login
   |
   v
Password Verification
   |
   v
JWT Access Token
   |
   v
Bearer Authentication
```

## Ownership Boundary

```text
User A
  |
  +-- Documents A
  |     |
  |     +-- Chunks A
  |
  +-- Conversations A
        |
        +-- Messages A

User B
  |
  +-- Documents B
  |     |
  |     +-- Chunks B
  |
  +-- Conversations B
        |
        +-- Messages B
```

All document retrieval, semantic retrieval, chat access, and conversation-history reads are scoped by the authenticated user's ID.

## Security Properties

- passwords are never stored in plaintext
- Argon2 password hashing
- JWT access tokens with expiration
- inactive accounts are rejected
- protected routes require bearer authentication
- document lookup is owner-scoped
- semantic retrieval joins through the authenticated user's documents
- conversation lookup is owner-scoped
- cross-user resources intentionally return not found

## Legacy Data

Existing v0.4.0 documents and conversations have no owner. The migration intentionally leaves their new owner fields null.

They are therefore invisible to authenticated users until reassigned or recreated. This avoids accidentally exposing legacy resources to a new account.
