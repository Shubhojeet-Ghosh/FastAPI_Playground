from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_TITLE: str = "FastAPI Playground"
    PROJECT_VERSION: str = "1.0"
    PORT: int = 8000
    RELOAD: bool = True
    HOST:str = "127.0.0.1"
    ENVIRONMENT: str

    class Config:
        env_file = ".env"

settings = Settings()