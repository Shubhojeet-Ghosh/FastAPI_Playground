from fastapi import APIRouter

from controllers.sgdevstudio_controller_files.clients_controller import *

sgdevstudio_router = APIRouter(prefix = "/sgdevstudio")

@sgdevstudio_router.get("/register-client" , status_code = 201)
async def register_new_client_route():
    return await register_new_client_controller()