from sqlalchemy.orm import Session

from app.core.config import settings
from app.repositories.conversation_repository import (
    add_message,
    create_conversation,
    get_conversation,
)
from app.schemas.chat import (
    AskResponse,
    ConversationHistoryResponse,
    MessageResponse,
    SourceCitation,
)
from app.services.llm_service import generate_grounded_answer
from app.services.retrieval_service import search_chunks


class ConversationNotFoundError(LookupError):
    pass


def _get_or_create_conversation(
    db: Session,
    conversation_id: int | None,
    question: str,
    user_id: int,
):
    if conversation_id is None:
        return create_conversation(
            db=db,
            user_id=user_id,
            title=question,
        )

    conversation = get_conversation(
        db=db,
        conversation_id=conversation_id,
        user_id=user_id,
    )

    if conversation is None:
        raise ConversationNotFoundError(
            f"Conversation {conversation_id} was not found."
        )

    return conversation


def _build_context(hits) -> str:
    blocks = []

    for index, hit in enumerate(hits, start=1):
        blocks.append(
            f"[{index}] Source: {hit.original_filename}\n"
            f"Chunk: {hit.chunk_index}\n"
            f"Content: {hit.content}"
        )

    return "\n\n".join(blocks)


def ask_knowledge_base(
    db: Session,
    question: str,
    user_id: int,
    conversation_id: int | None,
    top_k: int,
    min_similarity: float | None,
) -> AskResponse:
    conversation = _get_or_create_conversation(
        db=db,
        conversation_id=conversation_id,
        question=question,
        user_id=user_id,
    )

    add_message(
        db=db,
        conversation_id=conversation.id,
        role="user",
        content=question,
    )

    retrieval = search_chunks(
        db=db,
        query=question,
        top_k=min(top_k, settings.max_context_chunks),
        user_id=user_id,
        min_similarity=min_similarity,
    )

    if not retrieval.hits:
        answer = (
            "I don't have enough information in the indexed documents "
            "to answer that."
        )
        grounded = False
        sources = []
    else:
        context = _build_context(retrieval.hits)
        answer = generate_grounded_answer(
            question=question,
            context=context,
        )
        grounded = True
        sources = [
            SourceCitation(
                reference=index,
                chunk_id=hit.chunk_id,
                document_id=hit.document_id,
                original_filename=hit.original_filename,
                chunk_index=hit.chunk_index,
                similarity=hit.similarity,
            )
            for index, hit in enumerate(retrieval.hits, start=1)
        ]

    add_message(
        db=db,
        conversation_id=conversation.id,
        role="assistant",
        content=answer,
    )

    return AskResponse(
        conversation_id=conversation.id,
        question=question,
        answer=answer,
        sources=sources,
        grounded=grounded,
        llm_provider="groq",
        llm_model=settings.groq_model,
    )


def get_conversation_history(
    db: Session,
    conversation_id: int,
    user_id: int,
) -> ConversationHistoryResponse:
    conversation = get_conversation(
        db=db,
        conversation_id=conversation_id,
        user_id=user_id,
    )

    if conversation is None:
        raise ConversationNotFoundError(
            f"Conversation {conversation_id} was not found."
        )

    return ConversationHistoryResponse(
        conversation_id=conversation.id,
        title=conversation.title,
        messages=[
            MessageResponse.model_validate(message)
            for message in conversation.messages
        ],
    )
