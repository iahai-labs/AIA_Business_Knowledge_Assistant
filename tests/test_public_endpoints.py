from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_public_operational_endpoints() -> None:
    for path in ("/health", "/release"):
        response = client.get(path)
        assert response.status_code == 200
