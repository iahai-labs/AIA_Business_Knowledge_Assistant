from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI

import app.models  # noqa: F401
from app.api.documents import router as documents_router
from app.api.health import router as health_router
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine


@asynccontextmanager
async def lifespan(_: FastAPI):
    Path(settings.upload_dir).mkdir(parents=True, exist_ok=True)
    Base.metadata.create_all(bind=engine)
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        docs_url="/docs" if settings.debug else None,
        redoc_url="/redoc" if settings.debug else None,
        lifespan=lifespan,
    )
    app.include_router(health_router)
    app.include_router(documents_router, prefix="/api")
    return app


app = create_app()
