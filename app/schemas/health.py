from pydantic import BaseModel


class ProviderStatus(BaseModel):
    provider: str
    configured: bool
    model: str


class ProvidersHealthResponse(BaseModel):
    status: str
    providers: list[ProviderStatus]


class ReadinessResponse(BaseModel):
    status: str
    database: str
    jina_configured: bool
    groq_configured: bool
    jwt_configured: bool
