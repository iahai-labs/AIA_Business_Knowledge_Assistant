from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.models.user import User
from app.schemas.retrieval import RetrievalRequest, RetrievalResponse
from app.services.embedding_service import EmbeddingProviderError
from app.services.retrieval_service import search_chunks

router = APIRouter(prefix="/retrieval", tags=["retrieval"])


@router.post("/search", response_model=RetrievalResponse)
def semantic_search(
    payload: RetrievalRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> RetrievalResponse:
    try:
        return search_chunks(
            db=db,
            query=payload.query,
            top_k=payload.top_k,
            user_id=current_user.id,
            min_similarity=payload.min_similarity,
        )
    except EmbeddingProviderError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        ) from exc
