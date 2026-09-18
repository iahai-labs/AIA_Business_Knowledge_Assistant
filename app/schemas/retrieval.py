from pydantic import BaseModel, Field


class RetrievalRequest(BaseModel):
    query: str = Field(min_length=2, max_length=1000)
    top_k: int = Field(default=5, ge=1, le=20)


class RetrievalHit(BaseModel):
    chunk_id: int
    document_id: int
    original_filename: str
    chunk_index: int
    content: str
    similarity: float


class RetrievalResponse(BaseModel):
    query: str
    embedding_provider: str
    embedding_model: str
    hits: list[RetrievalHit]
    total: int
