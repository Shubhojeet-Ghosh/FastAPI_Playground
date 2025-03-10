from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_TITLE: str = "FastAPI Playground"
    PROJECT_VERSION: str = "1.0"
    PORT: int = 8000
    RELOAD: bool = True
    HOST:str = "0.0.0.0"
    ENVIRONMENT: str
    WORKERS: int = 2

    class Config:
        env_file = ".env"

settings = Settings()