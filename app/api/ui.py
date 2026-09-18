from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter(tags=["ui"])

UI_INDEX = Path(__file__).resolve().parent.parent / "ui" / "index.html"


@router.get("/", include_in_schema=False)
def web_app() -> FileResponse:
    return FileResponse(UI_INDEX, media_type="text/html")
