import logging
import time
from collections.abc import Callable
from typing import TypeVar

import httpx

from app.core.config import settings

T = TypeVar("T")

logger = logging.getLogger("aia.provider")


def run_with_http_retry(
    *,
    provider: str,
    operation: str,
    fn: Callable[[], T],
) -> T:
    attempts = max(1, settings.provider_retry_attempts)
    retryable_status_codes = {408, 425, 429, 500, 502, 503, 504}

    for attempt in range(1, attempts + 1):
        try:
            return fn()
        except httpx.HTTPStatusError as exc:
            status_code = exc.response.status_code
            retryable = status_code in retryable_status_codes

            logger.warning(
                "Provider HTTP error",
                extra={
                    "event": "provider_http_error",
                    "provider": provider,
                    "operation": operation,
                    "attempt": attempt,
                    "status_code": status_code,
                    "error_type": type(exc).__name__,
                },
            )

            if not retryable or attempt == attempts:
                raise
        except (
            httpx.ConnectError,
            httpx.ReadTimeout,
            httpx.WriteTimeout,
            httpx.PoolTimeout,
        ) as exc:
            logger.warning(
                "Provider network error",
                extra={
                    "event": "provider_network_error",
                    "provider": provider,
                    "operation": operation,
                    "attempt": attempt,
                    "error_type": type(exc).__name__,
                },
            )

            if attempt == attempts:
                raise

        delay = settings.provider_retry_backoff_seconds * (2 ** (attempt - 1))
        time.sleep(delay)

    raise RuntimeError("Retry loop exited unexpectedly.")
