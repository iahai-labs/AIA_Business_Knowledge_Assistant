from sqlalchemy.dialects import postgresql

from app.models.conversation import Conversation
from app.models.document import Document


def test_document_model_has_owner_column() -> None:
    assert hasattr(Document, "owner_user_id")


def test_conversation_model_has_owner_column() -> None:
    assert hasattr(Conversation, "owner_user_id")


def test_owner_columns_are_indexed() -> None:
    document_column = Document.__table__.c.owner_user_id
    conversation_column = Conversation.__table__.c.owner_user_id

    assert document_column.index is True
    assert conversation_column.index is True
