from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from src.Auth.Authentication import user_login
from src.pydantic_schema.User_pydantic import UserLogin

router = APIRouter()

@router.post("/")
def login(login_data: OAuth2PasswordRequestForm = Depends()):
   
    user = UserLogin(email=login_data.username, password=login_data.password)
    token = user_login(user)
    
    return {
        "access_token": token,
        "token_type": "bearer"
    }

    
