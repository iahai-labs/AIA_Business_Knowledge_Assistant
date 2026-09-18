from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.document import Document


def create_document(db: Session, document: Document) -> Document:
    db.add(document)
    db.commit()
    db.refresh(document)
    return document


def get_document_by_id(
    db: Session,
    document_id: int,
    user_id: int,
) -> Document | None:
    statement = select(Document).where(
        Document.id == document_id,
        Document.owner_user_id == user_id,
    )
    return db.scalar(statement)


def get_document_by_hash(
    db: Session,
    sha256: str,
    user_id: int,
) -> Document | None:
    statement = select(Document).where(
        Document.sha256 == sha256,
        Document.owner_user_id == user_id,
    )
    return db.scalar(statement)


def get_all_documents(
    db: Session,
    user_id: int,
) -> list[Document]:
    statement = (
        select(Document)
        .where(Document.owner_user_id == user_id)
        .order_by(Document.created_at.desc())
    )
    return list(db.scalars(statement).all())


def remove_document(db: Session, document: Document) -> None:
    db.delete(document)
    db.commit()
