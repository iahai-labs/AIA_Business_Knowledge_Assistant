from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.conversation import Conversation
from app.models.document import Document
from app.models.document_chunk import DocumentChunk
from app.models.message import Message
from app.models.user import User


def get_system_stats(db: Session) -> dict[str, int]:
    return {
        "users_total": db.scalar(select(func.count(User.id))) or 0,
        "users_active": db.scalar(
            select(func.count(User.id)).where(User.is_active.is_(True))
        ) or 0,
        "admins_total": db.scalar(
            select(func.count(User.id)).where(User.is_admin.is_(True))
        ) or 0,
        "documents_total": db.scalar(select(func.count(Document.id))) or 0,
        "indexed_chunks_total": db.scalar(select(func.count(DocumentChunk.id))) or 0,
        "conversations_total": db.scalar(select(func.count(Conversation.id))) or 0,
        "messages_total": db.scalar(select(func.count(Message.id))) or 0,
    }


def list_users_with_counts(db: Session) -> list[tuple[User, int, int]]:
    document_count = func.count(func.distinct(Document.id))
    conversation_count = func.count(func.distinct(Conversation.id))

    statement = (
        select(User, document_count, conversation_count)
        .outerjoin(Document, Document.owner_user_id == User.id)
        .outerjoin(Conversation, Conversation.owner_user_id == User.id)
        .group_by(User.id)
        .order_by(User.created_at.desc())
    )

    return [(row[0], int(row[1]), int(row[2])) for row in db.execute(statement).all()]


def list_documents_with_owner(db: Session) -> list[tuple[Document, str | None, int]]:
    chunk_count = func.count(DocumentChunk.id)

    statement = (
        select(Document, User.email, chunk_count)
        .outerjoin(User, User.id == Document.owner_user_id)
        .outerjoin(DocumentChunk, DocumentChunk.document_id == Document.id)
        .group_by(Document.id, User.email)
        .order_by(Document.created_at.desc())
    )

    return [(row[0], row[1], int(row[2])) for row in db.execute(statement).all()]


def list_conversations_with_owner(
    db: Session,
) -> list[tuple[Conversation, str | None, int]]:
    message_count = func.count(Message.id)

    statement = (
        select(Conversation, User.email, message_count)
        .outerjoin(User, User.id == Conversation.owner_user_id)
        .outerjoin(Message, Message.conversation_id == Conversation.id)
        .group_by(Conversation.id, User.email)
        .order_by(Conversation.created_at.desc())
    )

    return [(row[0], row[1], int(row[2])) for row in db.execute(statement).all()]
