from app.observability.logging import redact


def test_redact_masks_sensitive_values() -> None:
    payload = {
        "email": "demo@example.com",
        "access_token": "secret-token",
        "nested": {
            "password": "secret-password",
        },
    }

    redacted = redact(payload)

    assert redacted["email"] == "demo@example.com"
    assert redacted["access_token"] == "[REDACTED]"
    assert redacted["nested"]["password"] == "[REDACTED]"
