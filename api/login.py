from fastapi import APIRouter, Depends,HTTPException,status
from src.pydantic_schema.User_pydantic import UserLogin
from fastapi.security import OAuth2PasswordRequestForm
from src.Auth.Authentication import user_login
from src.pydantic_schema.User_pydantic import UserLogin

router = APIRouter()

@router.post("/")
def login(login_data: OAuth2PasswordRequestForm = Depends()):
    try:
        user = UserLogin(email=login_data.username, password=login_data.password)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invaild credantial !!")
    token = user_login(user)
    
    return {
        "access_token": token,
        "token_type": "bearer"
    }


    
