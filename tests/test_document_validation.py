from app.services.document_service import (
    DocumentValidationError,
    _validate_extension,
    _validate_size,
)


def test_validate_extension_accepts_pdf() -> None:
    assert _validate_extension("policy.pdf") == ".pdf"


def test_validate_extension_rejects_executable() -> None:
    try:
        _validate_extension("payload.exe")
        assert False, "Expected DocumentValidationError"
    except DocumentValidationError:
        assert True


def test_validate_size_rejects_empty_file() -> None:
    try:
        _validate_size(b"")
        assert False, "Expected DocumentValidationError"
    except DocumentValidationError:
        assert True
