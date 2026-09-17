from fastapi import APIRouter
from sqlalchemy import text

from app.core.config import settings
from app.db.session import SessionLocal

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
