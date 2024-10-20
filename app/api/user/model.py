from pydantic import BaseModel
from typing import Optional


class insert_user_request(BaseModel):
    u_name:str
    email:str
    password:str

class user_login_request(BaseModel):
    email:str
    password:str

class user_login_response(BaseModel):
    u_id:Optional[int]=None
    u_name:Optional[str]=None
    email:Optional[str]=None
    authorize:bool
    access_token: Optional[str] = None  # Add access_token field
    token_type: Optional[str] = None    # Add token_type field (e.g., "bearer")

class TokenData(BaseModel):
    user_id: int
    user_name: str