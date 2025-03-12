from fastapi import FastAPI
import uvicorn
import socketio

from settings import settings
from routes.main_router import *

sio = socketio.AsyncServer(cors_allowed_origins="*", async_mode="asgi")
socket_app = socketio.ASGIApp(sio)

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

app.mount("/socket.io", socket_app)

connected_clients = set()

@app.get("/")
def read_root():
    print("Hello. Welcome to FastAPI Playground.")
    return F"Welcome to FastAPI Playground {settings.ENVIRONMENT} environment, version {settings.PROJECT_VERSION}."

# Include the main router, which in turn includes all other route modules
app.include_router(main_router)

@sio.on("connect")
async def connect(sid, environ):
    connected_clients.add(sid)
    print(f"New client connected: {sid}.")

@sio.on("disconnect")
async def disconnect(sid):
    print(f"Client disconnected: {sid}")

@sio.on("mark-online")
async def register_user(sid, data):
    """Handles user registration event and broadcasts to all other clients."""
    
    print(f"Received register-user event from {sid}: {data}")

    # Validate incoming data format
    if not isinstance(data, dict) or "session_id" not in data:
        print("Invalid data format received")
        return
    
    session_id = data["session_id"]

    # Broadcast the session_id to all other connected clients except sender
    for client in connected_clients:
        if client != sid:
            await sio.emit("new-visitor-joined", {"session_id": session_id}, to=client)

    print(f"Broadcasted session_id {session_id} to all other clients")

if __name__ == "__main__":
    uvicorn.run("app:app",host=settings.HOST,port=settings.PORT,reload=settings.RELOAD,workers=settings.WORKERS)