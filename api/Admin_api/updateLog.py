from src.CRUD.User_crud import updatelog
from src.pydantic_schema.User_log_pydantic import add_log
from fastapi import APIRouter,HTTPException
from src.Dependancy.dependancy import user

router=APIRouter()

@router.post("/")
def updateLogFunc(log:add_log,current_user:dict = user):
    try:
        return updatelog(log=log,name=current_user["username"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))