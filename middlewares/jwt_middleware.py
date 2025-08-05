from fastapi import Request, HTTPException, status, Depends
import jwt  # PyJWT
from settings import settings

def authorize_user(request: Request):
    auth_header = request.headers.get("authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        print("Missing or invalid Authorization header")
        return None
    
    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        print("Token is valid...")
        return payload

    except jwt.ExpiredSignatureError:
        print("Token expired...")
        return None
    except jwt.InvalidTokenError:
        print("Invalid token...")
        return None
