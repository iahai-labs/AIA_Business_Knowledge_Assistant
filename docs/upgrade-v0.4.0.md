# Upgrade to v0.4.0

## Environment

Keep the Jina configuration from v0.3.1 and add:

```env
APP_VERSION=0.4.0

RETRIEVAL_MIN_SIMILARITY=0.25

GROQ_API_KEY=your-groq-api-key
GROQ_BASE_URL=https://api.groq.com/openai/v1
GROQ_MODEL=llama-3.1-8b-instant
GROQ_TIMEOUT_SECONDS=45
ANSWER_TEMPERATURE=0.1
MAX_CONTEXT_CHUNKS=5
```

## Rebuild

```powershell
docker compose down
docker compose build --no-cache
docker compose up -d
```

## Tests

```powershell
docker compose exec app pytest
```

The new `conversations` and `messages` tables are created automatically on application startup.

## Manual Test

Use Swagger:

```text
http://localhost:8000/docs
```

Run:

```text
POST /api/chat/ask
```

Example:

```json
{
  "question": "Can this company automate business tasks?",
  "top_k": 5
}
```

Then use the returned conversation ID with:

```text
GET /api/chat/conversations/{conversation_id}
```
