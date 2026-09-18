from app.schemas.retrieval import RetrievalHit
from app.services import retrieval_service


class FakeChunk:
    def __init__(self, chunk_id, document_id, filename, chunk_index, content):
        self.id = chunk_id
        self.document_id = document_id
        self.chunk_index = chunk_index
        self.content = content
        self.document = type("Document", (), {"original_filename": filename})()


def test_retrieval_filters_low_similarity(monkeypatch) -> None:
    monkeypatch.setattr(
        retrieval_service,
        "embed_query",
        lambda _: [0.1, 0.2],
    )

    rows = [
        (FakeChunk(1, 1, "good.txt", 0, "relevant"), 0.20),
        (FakeChunk(2, 2, "bad.txt", 0, "irrelevant"), 0.90),
    ]

    monkeypatch.setattr(
        retrieval_service,
        "semantic_search",
        lambda db, query_embedding, top_k: rows,
    )

    response = retrieval_service.search_chunks(
        db=None,
        query="business automation",
        top_k=5,
        min_similarity=0.5,
    )

    assert response.total == 1
    assert response.hits[0].original_filename == "good.txt"
