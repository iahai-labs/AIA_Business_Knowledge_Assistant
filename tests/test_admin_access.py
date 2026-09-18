import pytest
from fastapi import HTTPException

from app.api.deps import get_current_admin


class FakeUser:
    def __init__(self, is_admin: bool):
        self.is_admin = is_admin


def test_admin_dependency_accepts_admin() -> None:
    user = FakeUser(is_admin=True)
    assert get_current_admin(user) is user


def test_admin_dependency_rejects_non_admin() -> None:
    with pytest.raises(HTTPException) as exc_info:
        get_current_admin(FakeUser(is_admin=False))

    assert exc_info.value.status_code == 403
    assert exc_info.value.detail == "Administrator access required."
