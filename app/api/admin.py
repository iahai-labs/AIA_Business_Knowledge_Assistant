from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_admin, get_db
from app.models.user import User
from app.observability.metrics import get_metrics_snapshot
from app.schemas.metrics import RuntimeMetricsResponse
from app.schemas.admin import (
    AdminConversationResponse,
    AdminDocumentResponse,
    AdminStatsResponse,
    AdminUserResponse,
)
from app.services.admin_service import (
    admin_conversations,
    admin_documents,
    admin_users,
    system_stats,
)

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/stats", response_model=AdminStatsResponse)
def stats(
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin),
) -> AdminStatsResponse:
    return system_stats(db)


@router.get("/users", response_model=list[AdminUserResponse])
def users(
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin),
) -> list[AdminUserResponse]:
    return admin_users(db)


@router.get("/documents", response_model=list[AdminDocumentResponse])
def documents(
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin),
) -> list[AdminDocumentResponse]:
    return admin_documents(db)


@router.get("/conversations", response_model=list[AdminConversationResponse])
def conversations(
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin),
) -> list[AdminConversationResponse]:
    return admin_conversations(db)


@router.get("/metrics", response_model=RuntimeMetricsResponse)
def runtime_metrics(
    _: User = Depends(get_current_admin),
) -> RuntimeMetricsResponse:
    snapshot = get_metrics_snapshot()

    return RuntimeMetricsResponse(
        requests_total=snapshot.requests_total,
        errors_total=snapshot.errors_total,
        slow_requests_total=snapshot.slow_requests_total,
        average_duration_ms=round(snapshot.average_duration_ms, 2),
    )
