from logging_config import get_logger

from helpers.sgdevstudio_helper_files.sgdevstudio_user_helpers import *

async def register_new_client_controller():
    try:
        client_id = await generate_new_client_id()
        logger = get_logger(client_id)

        logger.info(f"Client ID Generated : {client_id}")

        register_client = await register_new_client_helper(client_id)
        logger.info(f"Registered Client : {register_client}")

        return ({"success":True,"message":"Client registered succesfully.","client_id":client_id})
    
    except Exception as e:
        logger.info(f"Something went wrong in register_new_client_controller: {e}")
        return({"success":False,"message" : "Something went wrong!"})