from src.CRUD.Admin_crud import Update_user_table,delete_user_table
from fastapi import APIRouter,HTTPException,status
from src.pydantic_schema.User_pydantic import EmailStr
from src.Dependancy.dependancy import admin

router=APIRouter()

@router.post("/")
def deletion(Email:EmailStr, current_user: dict = admin):
    try:
        master=current_user["username"]
        delete_user_table(user_email=Email,master=master)
        return {"message":"Deletion Done sucessfully"}
    except HTTPException as http:
        raise http
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))