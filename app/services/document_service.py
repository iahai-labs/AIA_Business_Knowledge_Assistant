import hashlib
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile
from pypdf import PdfReader
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.document import Document
from app.repositories.document_repository import (
    create_document,
    get_all_documents,
    get_document_by_hash,
    get_document_by_id,
    remove_document,
)


class DocumentValidationError(ValueError):
    pass


class DocumentNotFoundError(LookupError):
    pass


def _validate_extension(filename: str) -> str:
    extension = Path(filename).suffix.lower()

    if extension not in settings.allowed_extension_set:
        allowed = ", ".join(sorted(settings.allowed_extension_set))
        raise DocumentValidationError(
            f"Unsupported file type '{extension or 'unknown'}'. Allowed: {allowed}"
        )

    return extension


def _validate_size(content: bytes) -> None:
    max_bytes = settings.max_upload_mb * 1024 * 1024

    if not content:
        raise DocumentValidationError("The uploaded file is empty.")

    if len(content) > max_bytes:
        raise DocumentValidationError(
            f"File is too large. Maximum size is {settings.max_upload_mb} MB."
        )


def _extract_pdf_text(path: Path) -> tuple[str, int]:
    reader = PdfReader(str(path))
    pages: list[str] = []

    for page in reader.pages:
        pages.append(page.extract_text() or "")

    return "\n\n".join(pages).strip(), len(reader.pages)


def _extract_text(path: Path, extension: str) -> tuple[str, int | None]:
    if extension == ".pdf":
        return _extract_pdf_text(path)

    if extension in {".txt", ".md"}:
        return path.read_text(encoding="utf-8", errors="replace").strip(), None

    raise DocumentValidationError("No text extractor is configured for this file type.")


async def ingest_document(
    db: Session,
    file: UploadFile,
    user_id: int,
) -> Document:
    original_filename = file.filename or "unnamed"
    extension = _validate_extension(original_filename)

    content = await file.read()
    _validate_size(content)

    file_hash = hashlib.sha256(content).hexdigest()
    existing = get_document_by_hash(db, file_hash, user_id)

    if existing:
        raise DocumentValidationError(
            f"This document already exists with id={existing.id}."
        )

    upload_dir = Path(settings.upload_dir)
    upload_dir.mkdir(parents=True, exist_ok=True)

    stored_filename = f"{uuid4().hex}{extension}"
    stored_path = upload_dir / stored_filename
    stored_path.write_bytes(content)

    try:
        extracted_text, page_count = _extract_text(stored_path, extension)

        if not extracted_text:
            raise DocumentValidationError(
                "No readable text could be extracted from the document."
            )

        document = Document(
            owner_user_id=user_id,
            original_filename=original_filename,
            stored_filename=stored_filename,
            content_type=file.content_type,
            extension=extension,
            size_bytes=len(content),
            sha256=file_hash,
            status="ready",
            page_count=page_count,
            character_count=len(extracted_text),
            extracted_text=extracted_text,
        )

        return create_document(db, document)
    except Exception:
        stored_path.unlink(missing_ok=True)
        raise


def list_documents(
    db: Session,
    user_id: int,
) -> list[Document]:
    return get_all_documents(db, user_id)


def get_document(
    db: Session,
    document_id: int,
    user_id: int,
) -> Document:
    document = get_document_by_id(db, document_id, user_id)

    if document is None:
        raise DocumentNotFoundError(f"Document {document_id} was not found.")

    return document


def delete_document(
    db: Session,
    document_id: int,
    user_id: int,
) -> None:
    document = get_document(db, document_id, user_id)

    stored_path = Path(settings.upload_dir) / document.stored_filename
    stored_path.unlink(missing_ok=True)

    remove_document(db, document)
