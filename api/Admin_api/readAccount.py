from fastapi import APIRouter,HTTPException
from src.Dependancy.dependancy import both
from src.pydantic_schema.User_pydantic import EmailStr
from src.CRUD.Admin_crud import get_user

router = APIRouter()

@router.post("/")
def readAcount(Email:EmailStr,current_user:dict=both):
    try:
        return get_user(user_email=Email)
    except HTTPException as e:
        raise e
