from src.CRUD.User_crud import get_user_id,getlog_user
from src.pydantic_schema.User_log_pydantic import getlog
from fastapi import APIRouter,HTTPException
from src.Dependancy.dependancy import user

router=APIRouter()

@router.post("/")
def getloguser(current_user:dict = user):
    try:
        id=get_user_id(current_user["username"])
        return getlog_user(id=id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))