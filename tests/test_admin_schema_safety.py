from app.schemas.admin import AdminUserResponse


def test_admin_user_schema_does_not_expose_password_hash() -> None:
    fields = AdminUserResponse.model_fields
    assert "password_hash" not in fields
