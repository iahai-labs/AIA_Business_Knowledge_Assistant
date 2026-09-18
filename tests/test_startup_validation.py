import pytest

from app.core.config import settings
from app.core.startup_validation import (
    StartupConfigurationError,
    validate_startup_configuration,
)


def test_production_validation_rejects_weak_config(monkeypatch) -> None:
    monkeypatch.setattr(settings, "environment", "production")
    monkeypatch.setattr(settings, "debug", True)
    monkeypatch.setattr(settings, "jwt_secret_key", "short")
    monkeypatch.setattr(settings, "jina_api_key", "")
    monkeypatch.setattr(settings, "groq_api_key", "")
    monkeypatch.setattr(settings, "enable_hsts", False)
    monkeypatch.setattr(settings, "cors_allowed_origins", "*")
    monkeypatch.setattr(settings, "trusted_hosts", "*")

    with pytest.raises(StartupConfigurationError):
        validate_startup_configuration()
