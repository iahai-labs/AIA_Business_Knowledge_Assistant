from collections import defaultdict, deque
from threading import Lock
from time import monotonic

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.config import settings


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["Permissions-Policy"] = (
            "camera=(), microphone=(), geolocation=()"
        )
        response.headers["Cross-Origin-Resource-Policy"] = "same-origin"

        docs_paths = {
            "/docs",
            "/docs/oauth2-redirect",
            "/redoc",
            "/openapi.json",
        }

        if settings.debug and request.url.path in docs_paths:
            response.headers["Content-Security-Policy"] = (
                "default-src 'self'; "
                "img-src 'self' data: https:; "
                "style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; "
                "script-src 'self' 'unsafe-inline' "
                "https://cdn.jsdelivr.net https://cdn.redoc.ly; "
                "connect-src 'self'; "
                "font-src 'self' data: https://cdn.jsdelivr.net; "
                "frame-ancestors 'none'"
            )
        else:
            response.headers["Content-Security-Policy"] = (
                "default-src 'self'; "
                "img-src 'self' data:; "
                "style-src 'self' 'unsafe-inline'; "
                "script-src 'self' 'unsafe-inline'; "
                "connect-src 'self'; "
                "frame-ancestors 'none'"
            )

        if settings.enable_hsts:
            response.headers["Strict-Transport-Security"] = (
                "max-age=31536000; includeSubDomains"
            )

        return response


class RequestBodyLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        content_length = request.headers.get("content-length")

        if content_length:
            try:
                size = int(content_length)
            except ValueError:
                return JSONResponse(
                    status_code=400,
                    content={"detail": "Invalid Content-Length header."},
                )

            max_bytes = settings.max_request_body_mb * 1024 * 1024

            if size > max_bytes:
                return JSONResponse(
                    status_code=413,
                    content={"detail": "Request body is too large."},
                )

        return await call_next(request)


class InMemoryRateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self._requests = defaultdict(deque)
        self._lock = Lock()

    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith("/health") or request.url.path in {
            "/ready",
            "/release",
        }:
            return await call_next(request)

        client_host = request.client.host if request.client else "unknown"
        now = monotonic()
        window = max(1, settings.rate_limit_window_seconds)
        limit = max(1, settings.rate_limit_requests)

        with self._lock:
            bucket = self._requests[client_host]

            while bucket and bucket[0] <= now - window:
                bucket.popleft()

            if len(bucket) >= limit:
                return JSONResponse(
                    status_code=429,
                    content={"detail": "Rate limit exceeded. Try again later."},
                    headers={"Retry-After": str(window)},
                )

            bucket.append(now)

        return await call_next(request)
