from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_web_ui_is_available() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Business Knowledge Assistant" in response.text
    assert "Upload & index" in response.text
