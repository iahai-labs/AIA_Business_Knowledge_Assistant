from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.document_chunk import DocumentChunk
from app.repositories.chunk_repository import replace_document_chunks
from app.services.chunking_service import split_text
from app.services.document_service import get_document
from app.services.embedding_service import embed_documents


class DocumentIndexingError(RuntimeError):
    pass


def index_document(
    db: Session,
    document_id: int,
    user_id: int,
) -> dict[str, int | str]:
    document = get_document(
        db=db,
        document_id=document_id,
        user_id=user_id,
    )

    chunks = split_text(document.extracted_text)

    if not chunks:
        raise DocumentIndexingError("Document has no text available for indexing.")

    embeddings = embed_documents(chunks)

    chunk_models = [
        DocumentChunk(
            document_id=document.id,
            chunk_index=index,
            content=content,
            character_count=len(content),
            embedding=embedding,
        )
        for index, (content, embedding) in enumerate(zip(chunks, embeddings))
    ]

    replace_document_chunks(
        db=db,
        document_id=document.id,
        chunks=chunk_models,
    )

    return {
        "document_id": document.id,
        "chunks_created": len(chunk_models),
        "embedding_provider": settings.embedding_provider,
        "embedding_model": settings.embedding_model,
        "embedding_dimensions": settings.embedding_dimensions,
        "status": "indexed",
    }
