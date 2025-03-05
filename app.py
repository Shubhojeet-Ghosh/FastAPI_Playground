from fastapi import FastAPI
import uvicorn

from settings import settings
from routes.main_router import *

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

@app.get("/")
def read_root():
    print("Hello. Welcome to FastAPI Playground.")
    return F"Welcome to FastAPI Playground {settings.ENVIRONMENT} environment, version {settings.PROJECT_VERSION}."

# Include the main router, which in turn includes all other route modules
app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run(app,host=settings.HOST,port=settings.PORT,reload=settings.RELOAD)