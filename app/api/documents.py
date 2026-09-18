from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.models.user import User
from app.schemas.document import (
    DocumentIndexResponse,
    DocumentListResponse,
    DocumentResponse,
)
from app.services.document_service import (
    DocumentNotFoundError,
    DocumentValidationError,
    delete_document,
    get_document,
    ingest_document,
    list_documents,
)
from app.services.embedding_service import EmbeddingProviderError
from app.services.indexing_service import DocumentIndexingError, index_document

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post(
    "",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> DocumentResponse:
    try:
        document = await ingest_document(
            db=db,
            file=file,
            user_id=current_user.id,
        )
        return DocumentResponse.model_validate(document)
    except DocumentValidationError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc


@router.get("", response_model=DocumentListResponse)
def get_documents(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> DocumentListResponse:
    documents = list_documents(db, current_user.id)

    return DocumentListResponse(
        items=[DocumentResponse.model_validate(item) for item in documents],
        total=len(documents),
    )


@router.get("/{document_id}", response_model=DocumentResponse)
def get_document_by_id(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> DocumentResponse:
    try:
        document = get_document(
            db=db,
            document_id=document_id,
            user_id=current_user.id,
        )
        return DocumentResponse.model_validate(document)
    except DocumentNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


@router.post(
    "/{document_id}/index",
    response_model=DocumentIndexResponse,
)
def index_document_by_id(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> DocumentIndexResponse:
    try:
        return DocumentIndexResponse(
            **index_document(
                db=db,
                document_id=document_id,
                user_id=current_user.id,
            )
        )
    except DocumentNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except (DocumentIndexingError, EmbeddingProviderError) as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc


@router.delete("/{document_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_document(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> None:
    try:
        delete_document(
            db=db,
            document_id=document_id,
            user_id=current_user.id,
        )
    except DocumentNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
