from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from app.models.document_chunk import DocumentChunk


def replace_document_chunks(
    db: Session,
    document_id: int,
    chunks: list[DocumentChunk],
) -> list[DocumentChunk]:
    db.execute(
        delete(DocumentChunk).where(DocumentChunk.document_id == document_id)
    )
    db.add_all(chunks)
    db.commit()

    for chunk in chunks:
        db.refresh(chunk)

    return chunks


def semantic_search(
    db: Session,
    query_embedding: list[float],
    top_k: int,
) -> list[tuple[DocumentChunk, float]]:
    distance = DocumentChunk.embedding.cosine_distance(query_embedding).label("distance")

    statement = (
        select(DocumentChunk, distance)
        .order_by(distance)
        .limit(top_k)
    )

    rows = db.execute(statement).all()
    return [(row[0], float(row[1])) for row in rows]
