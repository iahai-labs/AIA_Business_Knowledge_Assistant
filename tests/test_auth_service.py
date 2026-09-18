from app.services.auth_service import normalize_email


def test_normalize_email() -> None:
    assert normalize_email("  USER@Example.COM ") == "user@example.com"
