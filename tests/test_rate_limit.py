from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.core.config import settings
from app.middleware.security import InMemoryRateLimitMiddleware


def test_rate_limit_blocks_after_limit(monkeypatch) -> None:
    monkeypatch.setattr(settings, "rate_limit_requests", 2)
    monkeypatch.setattr(settings, "rate_limit_window_seconds", 60)

    app = FastAPI()
    app.add_middleware(InMemoryRateLimitMiddleware)

    @app.get("/limited")
    def limited():
        return {"ok": True}

    client = TestClient(app)

    assert client.get("/limited").status_code == 200
    assert client.get("/limited").status_code == 200
    assert client.get("/limited").status_code == 429
