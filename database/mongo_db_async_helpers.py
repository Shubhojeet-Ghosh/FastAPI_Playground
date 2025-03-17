from database.connection import get_collection
from logging_config import get_logger
from datetime import datetime, timezone

logger = get_logger()

async def find_document(collection_name : str, query:dict):
    try:
        collection = get_collection(collection_name)

        document = await collection.find_one(query)

        if(document):
            return document
        
        else:
            return None
        
    except Exception as e:
        logger.info(f"Something went wrong : {e}")
        return None

async def insert_document(collection_name: str, insert_dict: dict):
    """
    Inserts a document into a MongoDB collection with 'created_at' timestamp if not present,
    and returns the full inserted document.

    :param collection_name: Name of the MongoDB collection
    :param insert_dict: Dictionary containing document data
    :return: The full inserted document or None if insertion failed
    """
    try:
        collection = get_collection(collection_name)

        # Ensure 'created_at' exists in a timezone-aware UTC format
        if "created_at" not in insert_dict:
            insert_dict["created_at"] = datetime.now(timezone.utc)

        insert_result = await collection.insert_one(insert_dict)

        if insert_result.inserted_id:
            # Fetch the inserted document using its _id
            inserted_document = await collection.find_one({"_id": insert_result.inserted_id})

            # Convert _id to string for better JSON serialization
            if inserted_document:
                inserted_document["_id"] = str(inserted_document["_id"])
            
            return inserted_document

        return None  # Return None if insertion fails

    except Exception as e:
        logger.error(f"Error inserting document into '{collection_name}': {e}")
        return None