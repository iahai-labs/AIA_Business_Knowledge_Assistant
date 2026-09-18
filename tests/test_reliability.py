import httpx

from app.core import reliability
from app.core.config import settings


def test_retry_eventually_succeeds(monkeypatch) -> None:
    monkeypatch.setattr(settings, "provider_retry_attempts", 3)
    monkeypatch.setattr(settings, "provider_retry_backoff_seconds", 0.0)

    attempts = {"count": 0}

    request = httpx.Request("GET", "https://example.com")
    retry_response = httpx.Response(
        503,
        request=request,
    )

    def flaky_call():
        attempts["count"] += 1

        if attempts["count"] < 3:
            raise httpx.HTTPStatusError(
                "temporary failure",
                request=request,
                response=retry_response,
            )

        return "ok"

    result = reliability.run_with_http_retry(
        provider="test",
        operation="test",
        fn=flaky_call,
    )

    assert result == "ok"
    assert attempts["count"] == 3
