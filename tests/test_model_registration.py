from app.db.base import Base
from app.models.document import Document


def test_document_model_is_registered() -> None:
    assert Document.__tablename__ == "documents"
    assert "documents" in Base.metadata.tables
