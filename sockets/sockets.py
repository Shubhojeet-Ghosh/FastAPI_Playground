import socketio

# Create Socket.IO instance
sio = socketio.AsyncServer(cors_allowed_origins="*", async_mode="asgi")

# Create ASGI app for Socket.IO
socketio_app = socketio.ASGIApp(sio)

# Set of connected clients
connected_clients = set()

# Handle 'connect' event
@sio.on("connect")
async def connect(sid, environ):
    connected_clients.add(sid)
    print(f"New client connected: {sid}. Updated Connected Clients : {connected_clients}")

# Handle 'disconnect' event
@sio.on("disconnect")
async def disconnect(sid):
    connected_clients.discard(sid)
    print(f"Client disconnected: {sid}.")

@sio.on("mark-online")
async def register_user(sid, data):
    """Handles user registration event and broadcasts to all other clients."""
    
    print(f"Received mark-online event from {sid}: {data}")

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