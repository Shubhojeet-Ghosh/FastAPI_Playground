from fastapi import APIRouter
from models.user_models.user import *
from controllers.user_controllers.user_controllers import *

user_router = APIRouter(prefix = "/users",tags=["Users"])

@user_router.post("/listen-user",status_code=201,response_model = ResponseFormat)
def listen_user_route(session_data : SessionInput):
    return listen_user_controller(session_data)
    