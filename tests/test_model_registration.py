from app.db.base import Base
from app.models.document import Document
from app.models.document_chunk import DocumentChunk


def test_models_are_registered() -> None:
    assert Document.__tablename__ == "documents"
    assert DocumentChunk.__tablename__ == "document_chunks"
    assert "documents" in Base.metadata.tables
    assert "document_chunks" in Base.metadata.tables
