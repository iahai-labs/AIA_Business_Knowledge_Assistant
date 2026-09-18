from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class AdminStatsResponse(BaseModel):
    users_total: int
    users_active: int
    admins_total: int
    documents_total: int
    indexed_chunks_total: int
    conversations_total: int
    messages_total: int


class AdminUserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    is_active: bool
    is_admin: bool
    created_at: datetime
    document_count: int
    conversation_count: int


class AdminDocumentResponse(BaseModel):
    id: int
    owner_user_id: int | None
    owner_email: EmailStr | None
    original_filename: str
    status: str
    size_bytes: int
    character_count: int
    created_at: datetime
    chunk_count: int


class AdminConversationResponse(BaseModel):
    id: int
    owner_user_id: int | None
    owner_email: EmailStr | None
    title: str
    created_at: datetime
    message_count: int
