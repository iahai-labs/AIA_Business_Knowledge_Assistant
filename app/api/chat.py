from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.models.user import User
from app.schemas.chat import AskRequest, AskResponse, ConversationHistoryResponse
from app.services.chat_service import (
    ConversationNotFoundError,
    ask_knowledge_base,
    get_conversation_history,
)
from app.services.embedding_service import EmbeddingProviderError
from app.services.llm_service import LLMProviderError

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/ask", response_model=AskResponse)
def ask(
    payload: AskRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> AskResponse:
    try:
        return ask_knowledge_base(
            db=db,
            question=payload.question,
            user_id=current_user.id,
            conversation_id=payload.conversation_id,
            top_k=payload.top_k,
            min_similarity=payload.min_similarity,
        )
    except EmbeddingProviderError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        ) from exc
    except LLMProviderError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        ) from exc
    except ConversationNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


@router.get(
    "/conversations/{conversation_id}",
    response_model=ConversationHistoryResponse,
)
def conversation_history(
    conversation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ConversationHistoryResponse:
    try:
        return get_conversation_history(
            db=db,
            conversation_id=conversation_id,
            user_id=current_user.id,
        )
    except ConversationNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
