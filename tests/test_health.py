from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    payload = response.json()

    assert payload["status"] == "ok"
    assert payload["service"] == "AIA Business Knowledge Assistant"
    assert payload["version"] == "1.0.0"

    assert response.headers["X-Request-ID"]
    assert response.headers["X-Process-Time-Ms"]
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "DENY"
