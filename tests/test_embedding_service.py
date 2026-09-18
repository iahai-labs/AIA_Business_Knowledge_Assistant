import httpx

from app.core.config import settings
from app.services import embedding_service


class FakeResponse:
    def __init__(self, payload: dict):
        self._payload = payload
        self.status_code = 200
        self.text = ""

    def raise_for_status(self) -> None:
        return None

    def json(self) -> dict:
        return self._payload


class FakeClient:
    def __init__(self, *args, **kwargs):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def post(self, url, headers, json):
        dimensions = json["dimensions"]
        data = [
            {"index": index, "embedding": [0.1] * dimensions}
            for index, _ in enumerate(json["input"])
        ]
        return FakeResponse({"data": data})


def test_jina_document_embeddings(monkeypatch) -> None:
    monkeypatch.setattr(settings, "jina_api_key", "test-key")
    monkeypatch.setattr(httpx, "Client", FakeClient)

    embeddings = embedding_service.embed_documents(["alpha", "beta"])

    assert len(embeddings) == 2
    assert len(embeddings[0]) == settings.embedding_dimensions


def test_jina_query_embedding(monkeypatch) -> None:
    monkeypatch.setattr(settings, "jina_api_key", "test-key")
    monkeypatch.setattr(httpx, "Client", FakeClient)

    embedding = embedding_service.embed_query("business services")

    assert len(embedding) == settings.embedding_dimensions
