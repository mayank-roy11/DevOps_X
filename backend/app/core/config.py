from functools import lru_cache
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Environment-driven configuration.

    We keep this simple for beginners but still production-aware:
    - All DB credentials come from env vars.
    - Optional `.env` is supported for local development.
    """

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = Field(default="Feedback Service", validation_alias="APP_NAME")
    environment: str = Field(default="development", validation_alias="ENVIRONMENT")
    debug: bool = Field(default=False, validation_alias="DEBUG")

    database_url: Optional[str] = Field(default=None, validation_alias="DATABASE_URL")
    db_host: str = Field(default="localhost", validation_alias="DB_HOST")
    db_port: int = Field(default=5432, validation_alias="DB_PORT")
    db_user: str = Field(default="postgres", validation_alias="DB_USER")
    db_password: str = Field(default="postgres", validation_alias="DB_PASSWORD")
    db_name: str = Field(default="feedback_db", validation_alias="DB_NAME")

    cors_allow_origins: str = Field(
        default="http://localhost:5173,http://localhost:3000",
        validation_alias="CORS_ALLOW_ORIGINS",
    )

    @property
    def sqlalchemy_database_url(self) -> str:
        """
        SQLAlchemy expects the `postgresql+psycopg2://` driver URL.
        """

        if self.database_url:
            return self.database_url

        return (
            f"postgresql+psycopg2://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )

    @property
    def cors_origins_list(self) -> list[str]:
        # Parse comma-separated origins from env var.
        return [o.strip() for o in self.cors_allow_origins.split(",") if o.strip()]


@lru_cache
def get_settings() -> Settings:
    # Use a cached settings object so it is created only once.
    return Settings()


settings = get_settings()

