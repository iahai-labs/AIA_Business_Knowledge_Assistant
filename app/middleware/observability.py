import logging
from time import perf_counter
from uuid import uuid4

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.config import settings
from app.observability.context import request_id_context
from app.observability.metrics import record_request

logger = logging.getLogger("aia.http")


class ObservabilityMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = request.headers.get("X-Request-ID") or uuid4().hex
        token = request_id_context.set(request_id)
        started = perf_counter()

        status_code = 500

        try:
            response = await call_next(request)
            status_code = response.status_code
            return response
        finally:
            duration_ms = (perf_counter() - started) * 1000
            is_error = status_code >= 500
            is_slow = duration_ms >= settings.request_slow_threshold_ms

            record_request(
                duration_ms=duration_ms,
                is_error=is_error,
                is_slow=is_slow,
            )

            extra = {
                "event": "request_complete",
                "method": request.method,
                "path": request.url.path,
                "status_code": status_code,
                "duration_ms": round(duration_ms, 2),
            }

            if is_error:
                logger.error("HTTP request failed", extra=extra)
            elif is_slow:
                logger.warning("Slow HTTP request", extra=extra)
            else:
                logger.info("HTTP request completed", extra=extra)

            try:
                response.headers["X-Request-ID"] = request_id
                response.headers["X-Process-Time-Ms"] = f"{duration_ms:.2f}"
            except UnboundLocalError:
                pass

            request_id_context.reset(token)
