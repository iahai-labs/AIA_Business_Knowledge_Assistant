# Upgrade to v1.1.0

Version 1.1.0 adds a minimal browser UI for the public portfolio demo.

## New UI

The application root now provides:

```text
/
```

Features:

- register and login
- JWT session stored in browser local storage
- document upload
- automatic indexing after upload
- document list
- grounded question answering
- source display
- safe no-context display

## Database

No schema migration is required.

## Environment

Update:

```env
APP_VERSION=1.1.0
```

Keep the existing production security and provider configuration.

## Deployment

On the server:

```bash
git pull
docker compose -f docker-compose.prod.yml build --no-cache
docker compose -f docker-compose.prod.yml up -d
```

Verify:

```bash
curl http://127.0.0.1:8001/health
curl http://127.0.0.1:8001/release
```

When deployed behind the existing Nginx path proxy, open:

```text
https://ai.iradhd.ir/work/business-knowledge-assistant/
```

## Public Demo Safety

The UI includes a warning not to upload confidential, personal, or sensitive business information.
