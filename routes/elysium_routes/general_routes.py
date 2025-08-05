from fastapi import APIRouter
from models.user_models.user import *
from controllers.user_controllers.user_controllers import *
from typing import Dict, Any
from controllers.elysium_chat_controllers.aws_controllers import generate_profile_image_presigned_url_controller
from middlewares.jwt_middleware import authorize_user
from fastapi import Depends

elysium_chat_router = APIRouter(prefix = "/elysium-chat",tags=["Elysium Chat"])

# Non async Method
@elysium_chat_router.post("/generate-profile-image-presigned-url")
def generate_profile_image_presigned_url_route(requestData: Dict[str, Any], user: dict = Depends(authorize_user)):
    return generate_profile_image_presigned_url_controller(requestData,user)