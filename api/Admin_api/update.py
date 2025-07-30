from src.CRUD.Admin_crud import Update_user_table
from fastapi import APIRouter
from src.pydantic_schema.User_pydantic import Update_user
from src.Dependancy.dependancy import admin

router=APIRouter()

@router.post("/")
def updation(user:Update_user, current_user: dict = admin):
    Update_user_table(user=user)
    return {"message":"Updation Done sucessfully"}
