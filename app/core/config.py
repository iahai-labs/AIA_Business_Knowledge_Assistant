from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AIA Business Knowledge Assistant"
    app_version: str = "0.7.0"
    environment: str = "development"
    debug: bool = True

    database_url: str = "postgresql+psycopg://aia:aia@db:5432/aia_knowledge"

    upload_dir: str = "uploads"
    max_upload_mb: int = 10
    allowed_extensions: str = ".pdf,.txt,.md"

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

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def allowed_extension_set(self) -> set[str]:
        return {
            item.strip().lower()
            for item in self.allowed_extensions.split(",")
            if item.strip()
        }


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
