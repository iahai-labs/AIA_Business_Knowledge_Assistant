from app.db.base import Base
from app.models.conversation import Conversation
from app.models.document import Document
from app.models.document_chunk import DocumentChunk
from app.models.message import Message


def test_models_are_registered() -> None:
    assert Document.__tablename__ == "documents"
    assert DocumentChunk.__tablename__ == "document_chunks"
    assert Conversation.__tablename__ == "conversations"
    assert Message.__tablename__ == "messages"

    assert "documents" in Base.metadata.tables
    assert "document_chunks" in Base.metadata.tables
    assert "conversations" in Base.metadata.tables
    assert "messages" in Base.metadata.tables
