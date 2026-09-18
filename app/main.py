import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import text
from starlette.middleware.trustedhost import TrustedHostMiddleware

import app.models  # noqa: F401
from app.api.admin import router as admin_router
from app.api.auth import router as auth_router
from app.api.chat import router as chat_router
from app.api.documents import router as documents_router
from app.api.health import router as health_router
from app.api.retrieval import router as retrieval_router
from app.api.release import router as release_router
from app.api.ui import router as ui_router
from app.core.config import settings
from app.core.startup_validation import validate_startup_configuration
from app.db.base import Base
from app.db.session import engine
from app.middleware.observability import ObservabilityMiddleware
from app.middleware.security import (
    InMemoryRateLimitMiddleware,
    RequestBodyLimitMiddleware,
    SecurityHeadersMiddleware,
)
from app.observability.logging import configure_logging

configure_logging()
logger = logging.getLogger("aia.app")


@asynccontextmanager
async def lifespan(_: FastAPI):
    validate_startup_configuration()

    Path(settings.upload_dir).mkdir(parents=True, exist_ok=True)

    with engine.begin() as connection:
        connection.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))

    Base.metadata.create_all(bind=engine)

    logger.info(
        "Application startup complete",
        extra={"event": "startup_complete"},
    )

    yield

    logger.info(
        "Application shutdown complete",
        extra={"event": "shutdown_complete"},
    )


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        docs_url="/docs" if settings.debug else None,
        redoc_url="/redoc" if settings.debug else None,
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origin_list,
        allow_credentials=False,
        allow_methods=["GET", "POST", "DELETE"],
        allow_headers=["Authorization", "Content-Type", "X-Request-ID"],
    )
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=settings.trusted_host_list,
    )
    app.add_middleware(SecurityHeadersMiddleware)
    app.add_middleware(RequestBodyLimitMiddleware)
    app.add_middleware(InMemoryRateLimitMiddleware)
    app.add_middleware(ObservabilityMiddleware)

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(
        request: Request,
        exc: Exception,
    ) -> JSONResponse:
        logger.exception(
            "Unhandled application exception",
            extra={
                "event": "unhandled_exception",
                "method": request.method,
                "path": request.url.path,
                "error_type": type(exc).__name__,
            },
        )

        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error."},
        )

    app.include_router(ui_router)
    app.include_router(health_router)
    app.include_router(release_router)
    app.include_router(auth_router, prefix="/api")
    app.include_router(admin_router, prefix="/api")
    app.include_router(documents_router, prefix="/api")
    app.include_router(retrieval_router, prefix="/api")
    app.include_router(chat_router, prefix="/api")

    return app


app = create_app()
