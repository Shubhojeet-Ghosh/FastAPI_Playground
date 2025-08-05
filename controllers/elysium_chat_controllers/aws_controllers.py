from logging_config import get_logger
from services.s3_service import *

from app_config.elysium_chat_config.chat_config import PUBLIC_BUCKET_NAME

def generate_profile_image_presigned_url_controller(requestData,user):
    try: 
        if(not user):
            return {
                "success": False,
                "message": "Invalid or expired token...",
            }
        
        logger = get_logger(user.get("email"))
        
        logger.info(f"User : {user.get('email')}")
        
        logger.info(f"Request Data : {requestData}")
        
        user_id = user.get("user_id")
        bucket_name = PUBLIC_BUCKET_NAME
        base_folder_location = f"profile_pictures/{user_id}/"
       
        file_name = requestData.get("file_name")
        file_type = requestData.get("file_type")
        if(not file_name or not file_type):
            return {
                "success": False,
                "message": "File name and file type are required..."
            }
        
        url_data = generate_presigned_upload_url(
            bucket_name=bucket_name,
            folder_path=base_folder_location,
            filename=file_name,
            filetype=file_type,
            expires_in=600
        )
        url_gen_status = url_data.get("status")
        
        if(url_gen_status == False):
            return {
                "success": False,
                "message": url_data.get("message")
            }
        
        upload_url = url_data.get("upload_url")
        s3_key = url_data.get("s3_key")
        s3_object_url = url_data.get("s3_object_url")

        return {
            "success": True,
            "message": "Presigned URL generated successfully",
            "presigned_url": upload_url,
            "s3_object_url": s3_object_url
        }
    
    except Exception as e:
        return {
            "success": False,
            "message": "Something went wrong...",
            "error": str(e)
        }