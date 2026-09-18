from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_release_info() -> None:
    response = client.get("/release")

    assert response.status_code == 200

    payload = response.json()

    assert payload["version"] == "0.9.0"
    assert payload["status"] == "release-candidate"
    assert "rag-retrieval" in payload["features"]
    assert "security-hardening" in payload["features"]
