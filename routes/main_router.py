from fastapi import APIRouter

from routes.user_routes.user_routes import user_router
from routes.sgdevstudio.sgdevstudio_routes import sgdevstudio_router
from routes.elysium_routes.general_routes import elysium_chat_router

# Create the main router with a prefix
main_router = APIRouter(prefix = "/fastapi-playground")

# Include the user router, ensuring all user-related routes are registered under the main prefix
main_router.include_router(user_router)

# Routes related to the portfolio web application sgdevstudio
main_router.include_router(sgdevstudio_router)

# Routes related to the elysium chat
main_router.include_router(elysium_chat_router)