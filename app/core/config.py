from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AIA Business Knowledge Assistant"
    app_version: str = "0.2.1"
    environment: str = "development"
    debug: bool = True

    database_url: str = "postgresql+psycopg://aia:aia@db:5432/aia_knowledge"

    upload_dir: str = "uploads"
    max_upload_mb: int = 10
    allowed_extensions: str = ".pdf,.txt,.md"

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
