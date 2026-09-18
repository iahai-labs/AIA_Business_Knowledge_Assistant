from app.services.document_service import (
    DocumentValidationError,
    _validate_extension,
    _validate_mime_type,
    _validate_size,
)


def test_validate_extension_accepts_pdf() -> None:
    assert _validate_extension("policy.pdf") == ".pdf"


def test_validate_extension_rejects_executable() -> None:
    with __import__("pytest").raises(DocumentValidationError):
        _validate_extension("payload.exe")


def test_validate_size_rejects_empty_file() -> None:
    with __import__("pytest").raises(DocumentValidationError):
        _validate_size(b"")


def test_validate_mime_type_accepts_pdf() -> None:
    _validate_mime_type("application/pdf")


def test_validate_mime_type_rejects_binary() -> None:
    with __import__("pytest").raises(DocumentValidationError):
        _validate_mime_type("application/octet-stream")
