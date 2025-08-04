from fastapi import APIRouter
from src.pydantic_schema.User_log_pydantic import add_log
from src.CRUD.User_crud import addLog
from src.Dependancy.dependancy import user

router=APIRouter()

@router.post("/")
def logSet(log:add_log,current_user:dict=user):
    addLog(log=log,name=current_user["username"])
    return {"message":"Log added Sucessfully !!}"}


   