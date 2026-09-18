from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
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
) -> DocumentResponse:
    try:
        document = await ingest_document(db=db, file=file)
        return DocumentResponse.model_validate(document)
    except DocumentValidationError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc


@router.get("", response_model=DocumentListResponse)
def get_documents(db: Session = Depends(get_db)) -> DocumentListResponse:
    documents = list_documents(db)
    return DocumentListResponse(
        items=[DocumentResponse.model_validate(item) for item in documents],
        total=len(documents),
    )


@router.get("/{document_id}", response_model=DocumentResponse)
def get_document_by_id(
    document_id: int,
    db: Session = Depends(get_db),
) -> DocumentResponse:
    try:
        return DocumentResponse.model_validate(get_document(db, document_id))
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
) -> DocumentIndexResponse:
    try:
        return DocumentIndexResponse(**index_document(db, document_id))
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
) -> None:
    try:
        delete_document(db, document_id)
    except DocumentNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
