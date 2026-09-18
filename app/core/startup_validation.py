from app.core.config import settings


class StartupConfigurationError(RuntimeError):
    pass


def validate_startup_configuration() -> None:
    errors: list[str] = []

    if settings.environment.lower() in {"production", "staging"}:
        if settings.debug:
            errors.append("DEBUG must be false outside development.")

        if not settings.jwt_secret_key:
            errors.append("JWT_SECRET_KEY is required.")

        if len(settings.jwt_secret_key) < 32:
            errors.append("JWT_SECRET_KEY must be at least 32 characters.")

        if not settings.jina_api_key:
            errors.append("JINA_API_KEY is required.")

        if not settings.groq_api_key:
            errors.append("GROQ_API_KEY is required.")

        if settings.enable_hsts is False:
            errors.append("ENABLE_HSTS should be true in production.")

        if "*" in settings.cors_origin_list:
            errors.append("Wildcard CORS origins are not allowed in production.")

        if "*" in settings.trusted_host_list:
            errors.append("Wildcard trusted hosts are not allowed in production.")

    if errors:
        raise StartupConfigurationError(
            "Invalid startup configuration: " + " ".join(errors)
        )
