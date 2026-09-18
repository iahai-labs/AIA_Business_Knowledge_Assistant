from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_documents_require_authentication() -> None:
    response = client.get("/api/documents")
    assert response.status_code == 401


def test_admin_requires_authentication() -> None:
    response = client.get("/api/admin/stats")
    assert response.status_code == 401
