from fastapi import FastAPI
import uvicorn

from settings import settings

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

@app.get("/")
def read_root():
    print("Hello. Welcome to FastAPI Playground.")
    return F"Welcome to FastAPI Playground {settings.ENVIRONMENT} environment, version {settings.PROJECT_VERSION}."

if __name__ == "__main__":
    uvicorn.run("app:app",host=settings.HOST,port=settings.PORT,reload=settings.RELOAD)