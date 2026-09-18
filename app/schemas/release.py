from pydantic import BaseModel


class ReleaseInfoResponse(BaseModel):
    name: str
    version: str
    environment: str
    status: str
    features: list[str]
