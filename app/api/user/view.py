from fastapi import APIRouter, HTTPException, Header, status, Depends
from app.api.user.model import TokenData, insert_user_request,user_login_request, user_login_response
from app.db.user import insert_user_indb, query_user_indb
from typing import Tuple, Optional
import jwt
import datetime


router = APIRouter(
    prefix="/user",
    tags=["users"],
)

SECRET_KEY = "abcd" 
ALGORITHM = "HS256"

def create_jwt_token(user_id: int, user_name: str) -> str:
    # Define token expiration time
    expire = datetime.datetime.now() + datetime.timedelta(hours=1)
    # Create the JWT payload
    payload = {
        "sub": user_id,
        "name": user_name,
        "exp": expire
    }
    # Encode the JWT
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

@router.post("/create_user")
def insert_user(rq:insert_user_request)->None:
    insert_user_indb(rq.u_name,rq.email,rq.password)

@router.post("/user_login")
def insert_user(rq:user_login_request)->user_login_response:
    user = query_user_indb(rq.email,rq.password)
    if user is not None:
        # Generate JWT token
        token = create_jwt_token(user.u_id, user.u_name)
        response = user_login_response(
            u_id=user.u_id,
            u_name=user.u_name,
            email=user.email,
            authorize=True,
            access_token=token,
            token_type="bearer"
        )
    else:
        response = user_login_response(
            u_id=None,
            u_name=None,
            email=None,
            authorize=False,
            access_token=None,
            token_type=None
        )
    
    return response

def get_current_user(authorization: Optional[str] = Header(None)) -> TokenData:
    print(authorization)
    if authorization is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header missing"
        )
    
    try:
        payload = jwt.decode(authorization, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        user_name = payload.get("name")
        
        if user_id is None or user_name is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )
        
        return TokenData(user_id=user_id, user_name=user_name)
    except (jwt.ExpiredSignatureError, jwt.PyJWTError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )