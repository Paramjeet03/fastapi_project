from fastapi import APIRouter
from src.pydantic_schema.User_pydantic import UserCreate ,UserOut
from src.Dependancy.dependancy import admin
from  fastapi import HTTPException
from src.CRUD.Admin_crud import new_User

router=APIRouter()
@router.post("/")
def create_account(user: UserCreate, current_user: dict = admin):
    try:
        new_User(user)
        return {"message": "User created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))