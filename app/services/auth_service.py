from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.models.user import User
from app.repositories.user_repository import (
    create_user,
    get_user_by_email,
)


class DuplicateEmailError(ValueError):
    pass


class AuthenticationError(ValueError):
    pass


def normalize_email(email: str) -> str:
    return email.strip().lower()


def register_user(
    db: Session,
    email: str,
    password: str,
) -> User:
    normalized_email = normalize_email(email)

    if get_user_by_email(db, normalized_email) is not None:
        raise DuplicateEmailError("An account with this email already exists.")

    user = User(
        email=normalized_email,
        password_hash=hash_password(password),
        is_active=True,
    )

    return create_user(db, user)


def authenticate_user(
    db: Session,
    email: str,
    password: str,
) -> tuple[str, int]:
    normalized_email = normalize_email(email)
    user = get_user_by_email(db, normalized_email)

    if user is None or not user.is_active:
        raise AuthenticationError("Invalid email or password.")

    if not verify_password(password, user.password_hash):
        raise AuthenticationError("Invalid email or password.")

    return create_access_token(user.id)
