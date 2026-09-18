# AIA Business Knowledge Assistant v0.2.1 Hotfix

This hotfix removes the circular import between `app.db.base` and `app.models.document`.

## Replace

- `app/db/base.py`
- `app/main.py`

## Add

- `tests/test_model_registration.py`

Then rebuild and test:

```powershell
docker compose down
docker compose build --no-cache
docker compose up -d
docker compose ps
docker compose exec app pytest
```
