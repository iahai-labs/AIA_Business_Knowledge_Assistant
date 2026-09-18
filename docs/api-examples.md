# API Examples

## Register

```http
POST /api/auth/register
Content-Type: application/json
```

```json
{
  "email": "demo@example.com",
  "password": "StrongDemoPassword123!"
}
```

## Login

```http
POST /api/auth/login
Content-Type: application/json
```

```json
{
  "email": "demo@example.com",
  "password": "StrongDemoPassword123!"
}
```

Use the returned access token as:

```text
Authorization: Bearer <access_token>
```

## Upload a Document

```http
POST /api/documents
Authorization: Bearer <access_token>
Content-Type: multipart/form-data
```

Upload any file from `demo_data/`.

## Index a Document

```http
POST /api/documents/{document_id}/index
Authorization: Bearer <access_token>
```

## Semantic Retrieval

```http
POST /api/retrieval/search
Authorization: Bearer <access_token>
Content-Type: application/json
```

```json
{
  "query": "Can the company automate lead follow-up?",
  "top_k": 5
}
```

## Grounded Answer

```http
POST /api/chat/ask
Authorization: Bearer <access_token>
Content-Type: application/json
```

```json
{
  "question": "Can the company automate repetitive business tasks?",
  "top_k": 5
}
```

## Safe Negative Query

```json
{
  "question": "What is the weather in Berlin today?",
  "top_k": 5
}
```

Expected behavior: the system should return an insufficient-information response and `grounded: false`.
