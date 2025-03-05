from pydantic import BaseModel, StringConstraints
from typing import Annotated

class SessionInput(BaseModel):
    session_id : Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]

class ResponseFormat(BaseModel):
    success:bool
    message:str