from app.db.base import Base
from app.models.conversation import Conversation
from app.models.document import Document
from app.models.document_chunk import DocumentChunk
from app.models.message import Message
from app.models.user import User


def test_models_are_registered() -> None:
    assert User.__tablename__ == "users"
    assert Document.__tablename__ == "documents"
    assert DocumentChunk.__tablename__ == "document_chunks"
    assert Conversation.__tablename__ == "conversations"
    assert Message.__tablename__ == "messages"

    assert "users" in Base.metadata.tables
    assert "documents" in Base.metadata.tables
    assert "document_chunks" in Base.metadata.tables
    assert "conversations" in Base.metadata.tables
    assert "messages" in Base.metadata.tables


def test_user_has_admin_flag() -> None:
    assert hasattr(User, "is_admin")
    assert User.__table__.c.is_admin.index is True
