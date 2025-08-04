from src.Dependancy.dependancy import admin
from fastapi import APIRouter,HTTPException
from src.pydantic_schema.task_pydantic import UpdateTask
from src.CRUD.Admin_crud import updateTask

router=APIRouter()

@router.post("/")
def taskUpdation(idx:int,task:UpdateTask,current_user:dict = admin):
    try:
        updateTask(idx=idx,updateTask=task)
        return {"message":"Task table updation sucessfully "}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))