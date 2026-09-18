import httpx

from app.core.config import settings
from app.services import llm_service


class FakeResponse:
    status_code = 200
    text = ""

    def raise_for_status(self):
        return None

    def json(self):
        return {
            "choices": [
                {
                    "message": {
                        "content": "The company provides AI automation services [1]."
                    }
                }
            ]
        }


class FakeClient:
    def __init__(self, *args, **kwargs):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def post(self, url, headers, json):
        return FakeResponse()


def test_generate_grounded_answer(monkeypatch) -> None:
    monkeypatch.setattr(settings, "groq_api_key", "test-key")
    monkeypatch.setattr(httpx, "Client", FakeClient)

    answer = llm_service.generate_grounded_answer(
        question="What services are offered?",
        context="[1] AI automation services",
    )

    assert "[1]" in answer
