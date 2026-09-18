from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.document import Document


def create_document(db: Session, document: Document) -> Document:
    db.add(document)
    db.commit()
    db.refresh(document)
    return document


def get_document_by_id(db: Session, document_id: int) -> Document | None:
    return db.get(Document, document_id)


def get_document_by_hash(db: Session, sha256: str) -> Document | None:
    statement = select(Document).where(Document.sha256 == sha256)
    return db.scalar(statement)


def get_all_documents(db: Session) -> list[Document]:
    statement = select(Document).order_by(Document.created_at.desc())
    return list(db.scalars(statement).all())


def remove_document(db: Session, document: Document) -> None:
    db.delete(document)
    db.commit()
