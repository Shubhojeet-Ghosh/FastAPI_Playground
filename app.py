from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from settings import settings
from routes.main_router import *
from sockets.sockets import socketio_app

# Initialize FastAPI
app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount Socket.IO application at /socket.io
app.mount("/socket.io", socketio_app)

@app.get("/")
def read_root():
    print("Hello. Welcome to FastAPI Playground.")
    return F"Welcome to FastAPI Playground {settings.ENVIRONMENT} environment, version {settings.PROJECT_VERSION}."

# Include the main router, which in turn includes all other route modules
app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run("app:app",host=settings.HOST,port=settings.PORT,reload=settings.RELOAD,workers=settings.WORKERS)