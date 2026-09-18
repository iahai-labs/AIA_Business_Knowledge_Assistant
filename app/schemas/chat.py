from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class AskRequest(BaseModel):
    question: str = Field(min_length=2, max_length=2000)
    conversation_id: int | None = None
    top_k: int = Field(default=5, ge=1, le=10)
    min_similarity: float | None = Field(default=None, ge=0.0, le=1.0)


class SourceCitation(BaseModel):
    reference: int
    chunk_id: int
    document_id: int
    original_filename: str
    chunk_index: int
    similarity: float


class AskResponse(BaseModel):
    conversation_id: int
    question: str
    answer: str
    sources: list[SourceCitation]
    grounded: bool
    llm_provider: str
    llm_model: str


class MessageResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    role: str
    content: str
    created_at: datetime


class ConversationHistoryResponse(BaseModel):
    conversation_id: int
    title: str
    messages: list[MessageResponse]
