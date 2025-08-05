from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    PROJECT_TITLE: str = "FastAPI Playground"
    PROJECT_VERSION: str = "0.0.4"
    PORT: int = 8000
    RELOAD: bool = Field(default=True)  # Pydantic will handle type conversion
    HOST: str = "0.0.0.0"
    ENVIRONMENT: str
    WORKERS: int = 2
    MONGO_URI: str
    MONGO_DB_NAME: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str
    JWT_SECRET: str
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"

settings = Settings()
