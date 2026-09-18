from app.core.config import settings
from app.api.health import provider_health_check


def test_provider_health_reports_configuration(monkeypatch) -> None:
    monkeypatch.setattr(settings, "jina_api_key", "jina-test-key")
    monkeypatch.setattr(settings, "groq_api_key", "groq-test-key")

    response = provider_health_check()

    assert response.status == "ok"
    assert len(response.providers) == 2
    assert all(provider.configured for provider in response.providers)
