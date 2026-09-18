from datetime import datetime, timedelta, timezone

import jwt
from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerifyMismatchError

from app.core.config import settings

password_hasher = PasswordHasher()


class TokenValidationError(RuntimeError):
    pass


def hash_password(password: str) -> str:
    return password_hasher.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    try:
        return password_hasher.verify(password_hash, password)
    except (VerifyMismatchError, InvalidHashError):
        return False


def create_access_token(user_id: int) -> tuple[str, int]:
    if not settings.jwt_secret_key:
        raise RuntimeError("JWT_SECRET_KEY is not configured.")

    expires_delta = timedelta(minutes=settings.jwt_access_token_minutes)
    expires_at = datetime.now(timezone.utc) + expires_delta

    payload = {
        "sub": str(user_id),
        "iat": datetime.now(timezone.utc),
        "exp": expires_at,
        "type": "access",
    }

    token = jwt.encode(
        payload,
        settings.jwt_secret_key,
        algorithm=settings.jwt_algorithm,
    )

    return token, int(expires_delta.total_seconds())


def decode_access_token(token: str) -> int:
    if not settings.jwt_secret_key:
        raise TokenValidationError("JWT authentication is not configured.")

    try:
        payload = jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=[settings.jwt_algorithm],
        )
    except jwt.ExpiredSignatureError as exc:
        raise TokenValidationError("Access token has expired.") from exc
    except jwt.PyJWTError as exc:
        raise TokenValidationError("Invalid access token.") from exc

    if payload.get("type") != "access":
        raise TokenValidationError("Invalid token type.")

    subject = payload.get("sub")

    try:
        return int(subject)
    except (TypeError, ValueError) as exc:
        raise TokenValidationError("Invalid token subject.") from exc
