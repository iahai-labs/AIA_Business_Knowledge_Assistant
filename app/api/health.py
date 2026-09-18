from fastapi import APIRouter, HTTPException, status
from sqlalchemy import text

from app.core.config import settings
from app.db.session import SessionLocal
from app.schemas.health import (
    ProviderStatus,
    ProvidersHealthResponse,
    ReadinessResponse,
)

router = APIRouter(tags=["health"])


@router.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": settings.app_name,
        "version": settings.app_version,
    }


@router.get("/health/db")
def database_health_check() -> dict[str, str]:
    with SessionLocal() as session:
        session.execute(text("SELECT 1"))

    return {
        "status": "ok",
        "database": "reachable",
    }


@router.get("/health/providers", response_model=ProvidersHealthResponse)
def provider_health_check() -> ProvidersHealthResponse:
    providers = [
        ProviderStatus(
            provider="jina",
            configured=bool(settings.jina_api_key),
            model=settings.embedding_model,
        ),
        ProviderStatus(
            provider="groq",
            configured=bool(settings.groq_api_key),
            model=settings.groq_model,
        ),
    ]

    overall = "ok" if all(item.configured for item in providers) else "degraded"

    return ProvidersHealthResponse(
        status=overall,
        providers=providers,
    )


@router.get("/ready", response_model=ReadinessResponse)
def readiness_check() -> ReadinessResponse:
    try:
        with SessionLocal() as session:
            session.execute(text("SELECT 1"))
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database is not ready.",
        ) from exc

    jina_configured = bool(settings.jina_api_key)
    groq_configured = bool(settings.groq_api_key)
    jwt_configured = bool(settings.jwt_secret_key)

    ready = jina_configured and groq_configured and jwt_configured

    if not ready:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={
                "status": "not_ready",
                "database": "reachable",
                "jina_configured": jina_configured,
                "groq_configured": groq_configured,
                "jwt_configured": jwt_configured,
            },
        )

    return ReadinessResponse(
        status="ready",
        database="reachable",
        jina_configured=True,
        groq_configured=True,
        jwt_configured=True,
    )
