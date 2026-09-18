from app.observability.metrics import get_metrics_snapshot, record_request


def test_record_request_updates_runtime_metrics() -> None:
    before = get_metrics_snapshot()

    record_request(
        duration_ms=100.0,
        is_error=True,
        is_slow=False,
    )

    after = get_metrics_snapshot()

    assert after.requests_total == before.requests_total + 1
    assert after.errors_total == before.errors_total + 1
