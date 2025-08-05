import boto3
from fastapi import HTTPException
from settings import settings

def generate_presigned_upload_url(
    bucket_name: str,
    folder_path: str,       # e.g. "images/user/"
    filename: str,          # e.g. "chat_icon3.png"
    filetype: str,          # e.g. "image/png"
    expires_in: int = 600   # 10 mins default
):
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION
    )
    # S3 object key (path inside the bucket)
    s3_key = f"{folder_path.rstrip('/')}/{filename}"

    try:
        params = {
            "Bucket": bucket_name,
            "Key": s3_key,
            "ContentType": filetype,
        }
        url = s3_client.generate_presigned_url(
            "put_object",
            Params=params,
            ExpiresIn=expires_in,
            HttpMethod="PUT"
        )
        return {
            "status": True,
            "upload_url": url,
            "s3_key": s3_key
        }
    except Exception as e:
        return {
            "status": False,
            "message": str(e)
        }

def construct_s3_object_url(
    bucket_name: str,
    file_key: str,
    region_name: str = settings.AWS_REGION
) -> str:
    """
    Constructs the public S3 object URL from bucket, region, and file key.
    """
    return f"https://{bucket_name}.s3.{region_name}.amazonaws.com/{file_key}"    