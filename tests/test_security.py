from app.core import security
from app.core.config import settings


def test_password_hash_and_verify() -> None:
    password = "a-strong-demo-password"
    password_hash = security.hash_password(password)

    assert password_hash != password
    assert security.verify_password(password, password_hash) is True
    assert security.verify_password("wrong-password", password_hash) is False


def test_access_token_round_trip(monkeypatch) -> None:
    monkeypatch.setattr(settings, "jwt_secret_key", "test-secret-key-that-is-long-enough")

    token, expires_in = security.create_access_token(user_id=42)
    user_id = security.decode_access_token(token)

    assert user_id == 42
    assert expires_in > 0
