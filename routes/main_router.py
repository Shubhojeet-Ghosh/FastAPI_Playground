from fastapi import APIRouter
from routes.user_routes.user_routes import user_router

# Create the main router with a prefix
main_router = APIRouter(prefix = "/fastapi-playground")

# Include the user router, ensuring all user-related routes are registered under the main prefix
main_router.include_router(user_router)