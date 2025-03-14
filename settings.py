from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    PROJECT_TITLE: str = "FastAPI Playground"
    PROJECT_VERSION: str = "1.0"
    PORT: int = 8000
    RELOAD: bool = Field(default=True)  # Pydantic will handle type conversion
    HOST: str = "0.0.0.0"
    ENVIRONMENT: str
    WORKERS: int = 2

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"

settings = Settings()
