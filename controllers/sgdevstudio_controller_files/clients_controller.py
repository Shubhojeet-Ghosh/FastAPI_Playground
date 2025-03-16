from logging_config import get_logger

from helpers.sgdevstudio_helper_files.sgdevstudio_user_helpers import generate_new_client_id

async def register_new_client_controller():
    try:
        client_id = generate_new_client_id()

        logger = get_logger()

        logger.info(f"Registering new client with session id : {client_id}")
        return ({"success":True,"message":"Client registered succesfully.","client_id":client_id})
    
    except Exception as e:
        print(f"Something went wrong : {e}")
        return({"success":False,"message" : "Something went wrong!"})