from sqlalchemy.orm import Session

from app.core.config import settings
from app.repositories.chunk_repository import semantic_search
from app.schemas.retrieval import RetrievalHit, RetrievalResponse
from app.services.embedding_service import embed_query


def search_chunks(
    db: Session,
    query: str,
    top_k: int,
    min_similarity: float | None = None,
) -> RetrievalResponse:
    threshold = (
        settings.retrieval_min_similarity
        if min_similarity is None
        else min_similarity
    )

    query_embedding = embed_query(query)
    rows = semantic_search(
        db=db,
        query_embedding=query_embedding,
        top_k=top_k,
    )

    hits = []

    for chunk, distance in rows:
        similarity = max(0.0, min(1.0, 1.0 - distance))

        if similarity < threshold:
            continue

        hits.append(
            RetrievalHit(
                chunk_id=chunk.id,
                document_id=chunk.document_id,
                original_filename=chunk.document.original_filename,
                chunk_index=chunk.chunk_index,
                content=chunk.content,
                similarity=similarity,
            )
        )

    return RetrievalResponse(
        query=query,
        embedding_provider=settings.embedding_provider,
        embedding_model=settings.embedding_model,
        min_similarity=threshold,
        hits=hits,
        total=len(hits),
    )
