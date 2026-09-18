# Upgrade to v0.3.1

## 1. Update environment settings

Keep your current database and upload settings, then add:

```env
APP_VERSION=0.3.1

EMBEDDING_PROVIDER=jina
JINA_API_KEY=your-jina-api-key
JINA_BASE_URL=https://api.jina.ai/v1
EMBEDDING_MODEL=jina-embeddings-v5-text-small
EMBEDDING_DIMENSIONS=1024
EMBEDDING_TIMEOUT_SECONDS=30
```

Remove the old OpenAI embedding settings if they are no longer used.

## 2. Rebuild dependencies

```powershell
docker compose down
docker compose build --no-cache
```

## 3. Reset the old vector table

Version 0.3.0 defined 1536-dimensional vectors. Version 0.3.1 uses 1024 dimensions.

If no successful v0.3.0 indexing occurred, run:

```powershell
docker compose up -d db
docker compose exec db psql -U aia -d aia_knowledge -c "DROP TABLE IF EXISTS document_chunks;"
docker compose down
```

This removes vector chunks only. It does not remove the `documents` table.

## 4. Start the application

```powershell
docker compose up -d
```

## 5. Test

```powershell
docker compose exec app pytest
```

## 6. Index and retrieve

Use Swagger:

```text
http://localhost:8000/docs
```

Run:

```text
POST /api/documents/{document_id}/index
POST /api/retrieval/search
```
