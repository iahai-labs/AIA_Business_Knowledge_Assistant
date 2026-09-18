from sqlalchemy.orm import Session

from app.repositories.admin_repository import (
    get_system_stats,
    list_conversations_with_owner,
    list_documents_with_owner,
    list_users_with_counts,
)
from app.schemas.admin import (
    AdminConversationResponse,
    AdminDocumentResponse,
    AdminStatsResponse,
    AdminUserResponse,
)


def system_stats(db: Session) -> AdminStatsResponse:
    return AdminStatsResponse(**get_system_stats(db))


def admin_users(db: Session) -> list[AdminUserResponse]:
    return [
        AdminUserResponse(
            id=user.id,
            email=user.email,
            is_active=user.is_active,
            is_admin=user.is_admin,
            created_at=user.created_at,
            document_count=document_count,
            conversation_count=conversation_count,
        )
        for user, document_count, conversation_count in list_users_with_counts(db)
    ]


def admin_documents(db: Session) -> list[AdminDocumentResponse]:
    return [
        AdminDocumentResponse(
            id=document.id,
            owner_user_id=document.owner_user_id,
            owner_email=owner_email,
            original_filename=document.original_filename,
            status=document.status,
            size_bytes=document.size_bytes,
            character_count=document.character_count,
            created_at=document.created_at,
            chunk_count=chunk_count,
        )
        for document, owner_email, chunk_count in list_documents_with_owner(db)
    ]


def admin_conversations(db: Session) -> list[AdminConversationResponse]:
    return [
        AdminConversationResponse(
            id=conversation.id,
            owner_user_id=conversation.owner_user_id,
            owner_email=owner_email,
            title=conversation.title,
            created_at=conversation.created_at,
            message_count=message_count,
        )
        for conversation, owner_email, message_count in list_conversations_with_owner(db)
    ]
