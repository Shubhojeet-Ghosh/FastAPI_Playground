from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import HTTPException

from settings import settings

from logging_config import get_logger
logger = get_logger()

MONGO_URI = settings.MONGO_URI
MONGO_DB_NAME = settings.MONGO_DB_NAME

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB_NAME]

def get_collection(collection_name: str):
    try:
        
        return db[collection_name]

    except Exception as e:
        logger.info(f"Something went wrong in get_collection : {e}")
        raise HTTPException(status_code=500, detail="Unexpected server error : {e}")