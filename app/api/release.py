from fastapi import APIRouter

from app.core.config import settings
from app.schemas.release import ReleaseInfoResponse

router = APIRouter(tags=["release"])


@router.get("/release", response_model=ReleaseInfoResponse)
def release_info() -> ReleaseInfoResponse:
    return ReleaseInfoResponse(
        name=settings.app_name,
        version=settings.app_version,
        environment=settings.environment,
        status="stable",
        features=[
            "authentication",
            "user-ownership",
            "rag-retrieval",
            "grounded-answers",
            "admin-workflows",
            "observability",
            "security-hardening",
        ],
    )
