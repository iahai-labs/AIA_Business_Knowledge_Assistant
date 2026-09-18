from functools import lru_cache

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AIA Business Knowledge Assistant"
    app_version: str = "0.9.0"
    environment: str = "development"
    debug: bool = True

    database_url: str = "postgresql+psycopg://aia:aia@db:5432/aia_knowledge"

    upload_dir: str = "uploads"
    max_upload_mb: int = 10
    allowed_extensions: str = ".pdf,.txt,.md"
    allowed_mime_types: str = "application/pdf,text/plain,text/markdown"

    embedding_provider: str = "jina"
    jina_api_key: str = ""
    jina_base_url: str = "https://api.jina.ai/v1"
    embedding_model: str = "jina-embeddings-v5-text-small"
    embedding_dimensions: int = 1024
    embedding_timeout_seconds: float = 30.0

    chunk_size: int = 1200
    chunk_overlap: int = 200
    retrieval_top_k: int = 5
    retrieval_min_similarity: float = 0.25

    groq_api_key: str = ""
    groq_base_url: str = "https://api.groq.com/openai/v1"
    groq_model: str = "openai/gpt-oss-120b"
    groq_timeout_seconds: float = 45.0
    answer_temperature: float = 0.1
    max_context_chunks: int = 5

    jwt_secret_key: str = ""
    jwt_algorithm: str = "HS256"
    jwt_access_token_minutes: int = 60

    log_level: str = "INFO"
    log_json: bool = True
    provider_retry_attempts: int = 3
    provider_retry_backoff_seconds: float = 0.4
    request_slow_threshold_ms: float = 1500.0

    cors_allowed_origins: str = "http://localhost:3000,http://localhost:8000"
    rate_limit_requests: int = 60
    rate_limit_window_seconds: int = 60
    max_request_body_mb: int = 12
    trusted_hosts: str = "localhost,127.0.0.1"
    enable_hsts: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @field_validator("jwt_secret_key")
    @classmethod
    def validate_jwt_secret(cls, value: str, info):
        if not value:
            return value
        if len(value) < 32:
            raise ValueError("JWT_SECRET_KEY must be at least 32 characters.")
        return value

    @property
    def allowed_extension_set(self) -> set[str]:
        return {
            item.strip().lower()
            for item in self.allowed_extensions.split(",")
            if item.strip()
        }

    @property
    def allowed_mime_type_set(self) -> set[str]:
        return {
            item.strip().lower()
            for item in self.allowed_mime_types.split(",")
            if item.strip()
        }

    @property
    def cors_origin_list(self) -> list[str]:
        return [
            item.strip()
            for item in self.cors_allowed_origins.split(",")
            if item.strip()
        ]

    @property
    def trusted_host_list(self) -> list[str]:
        return [
            item.strip()
            for item in self.trusted_hosts.split(",")
            if item.strip()
        ]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
