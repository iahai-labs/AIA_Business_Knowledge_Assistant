from sqlalchemy.orm import Session

from app.core.config import settings
from app.repositories.chunk_repository import semantic_search
from app.schemas.retrieval import RetrievalHit, RetrievalResponse
from app.services.embedding_service import embed_query


def search_chunks(
    db: Session,
    query: str,
    top_k: int,
) -> RetrievalResponse:
    query_embedding = embed_query(query)
    rows = semantic_search(
        db=db,
        query_embedding=query_embedding,
        top_k=top_k,
    )

    hits = [
        RetrievalHit(
            chunk_id=chunk.id,
            document_id=chunk.document_id,
            original_filename=chunk.document.original_filename,
            chunk_index=chunk.chunk_index,
            content=chunk.content,
            similarity=max(0.0, min(1.0, 1.0 - distance)),
        )
        for chunk, distance in rows
    ]

    return RetrievalResponse(
        query=query,
        embedding_provider=settings.embedding_provider,
        embedding_model=settings.embedding_model,
        hits=hits,
        total=len(hits),
    )
