# Upgrade to v0.3.0

If upgrading an existing v0.2.1 working directory, keep your existing `.env` and add the new embedding and retrieval settings.

Recommended steps:

```powershell
docker compose down
docker compose build --no-cache
docker compose up -d
docker compose exec app pytest
```

No existing `documents` data needs to be deleted.

The application creates the `vector` extension and the new `document_chunks` table on startup.

Before indexing documents, configure `OPENAI_API_KEY` and verify that your selected provider supports the configured embeddings model.
