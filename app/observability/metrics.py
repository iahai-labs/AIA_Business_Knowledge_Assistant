from dataclasses import dataclass
from threading import Lock


@dataclass
class MetricsSnapshot:
    requests_total: int
    errors_total: int
    slow_requests_total: int
    total_duration_ms: float

    @property
    def average_duration_ms(self) -> float:
        if self.requests_total == 0:
            return 0.0
        return self.total_duration_ms / self.requests_total


_lock = Lock()
_requests_total = 0
_errors_total = 0
_slow_requests_total = 0
_total_duration_ms = 0.0


def record_request(
    *,
    duration_ms: float,
    is_error: bool,
    is_slow: bool,
) -> None:
    global _requests_total
    global _errors_total
    global _slow_requests_total
    global _total_duration_ms

    with _lock:
        _requests_total += 1
        _total_duration_ms += duration_ms

        if is_error:
            _errors_total += 1

        if is_slow:
            _slow_requests_total += 1


def get_metrics_snapshot() -> MetricsSnapshot:
    with _lock:
        return MetricsSnapshot(
            requests_total=_requests_total,
            errors_total=_errors_total,
            slow_requests_total=_slow_requests_total,
            total_duration_ms=_total_duration_ms,
        )
