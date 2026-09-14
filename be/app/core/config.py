from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "CariKampus"
    APP_ENV: str = "development"
    API_V1_STR: str = "/api/v1"

    DATABASE_URL: str = ""

    FRONTEND_URLS: str = "http://localhost:3000,http://127.0.0.1:3000"

    @property
    def cors_origins(self) -> List[str]:
        if not self.FRONTEND_URLS:
            return ["*"]
        return [url.strip() for url in self.FRONTEND_URLS.split(",") if url.strip()]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()
