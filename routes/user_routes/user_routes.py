from fastapi import APIRouter
from models.user_models.user import *
from controllers.user_controllers.user_controllers import *

user_router = APIRouter(prefix = "/users",tags=["Users"])

# Non async Method
@user_router.post("/listen-user",status_code=201,response_model = ResponseFormat)
def listen_user_route(session_data : SessionInput):
    return listen_user_controller(session_data)

# Async method
@user_router.post("/listen-user-async",status_code=201,response_model = ResponseFormat)
async def listen_user_async_route(session_data : SessionInput):
    return await listen_user_async_controller(session_data)