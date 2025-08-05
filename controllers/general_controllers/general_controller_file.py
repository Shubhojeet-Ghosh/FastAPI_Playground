from logging_config import get_logger
from services.s3_service import generate_presigned_upload_url

def generate_profile_image_presigned_url_controller(requestData):
    try: 
        logger = get_logger()
        logger.info(f"Request Data : {requestData}")
        
        bucket_name = requestData.get("bucket_name")
        folder_location = requestData.get("folder_location")
        file_name = requestData.get("file_name")
        expires_in = requestData.get("expires_in")

        url = generate_presigned_upload_url(
            bucket_name=bucket_name,
            folder_location=folder_location,
            file_name=file_name,
            expires_in=expires_in
        )
        
    except Exception as e:
        return {
            "success": False,
            "message": "Something went wrong...",
            "error": str(e)
        }