from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        docs_url="/docs" if settings.debug else None,
        redoc_url="/redoc" if settings.debug else None,
    )
    app.include_router(health_router)
    return app


app = create_app()
