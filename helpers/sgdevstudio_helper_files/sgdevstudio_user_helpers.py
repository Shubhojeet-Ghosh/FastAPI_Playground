import secrets
from database.connection import get_collection
from database.mongo_db_async_helpers import *
from database.collections import *
async def generate_new_client_id():
    try:
        while True:
            potential_client_id = secrets.token_hex(10)
            collection_name = sgdevstudio_clients
            query = {
                "client_id" : potential_client_id
            }
            client_id_exists = await find_document(collection_name,query)

            if(client_id_exists):
                continue
            
            else:
                break

        return f"cl-{potential_client_id}"    
            
    except Exception as e:
        logger.info(f"Something went wrong in generate_new_client_id : {e}")
        return None

async def register_new_client_helper(client_id : str):
    try:
        logger = get_logger(client_id)

        collection_name = sgdevstudio_clients

        insert_dict = {
            "client_id":client_id
        }
        insert_result = await insert_document(collection_name , insert_dict)
        
        return insert_result
    
    except Exception as e:
        logger.info(f"Something went wrong in register_new_client_controller: {e}")
        return False