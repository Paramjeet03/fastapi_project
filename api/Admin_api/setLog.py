from fastapi import APIRouter
from src.pydantic_schema.User_pydantic import log_detail
from src.CRUD.User_crud import addLog
from src.Dependancy.dependancy import user

router=APIRouter()

@router.post("/")
def logSet(log:log_detail,current_user:dict=user):
    addLog(log=log)
    return {"message":"Log added Sucessfully !!"}