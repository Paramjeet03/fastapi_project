from src.CRUD.Admin_crud import assignTask
from src.pydantic_schema.task_pydantic import TaskCreate
from fastapi import APIRouter,HTTPException
from src.Dependancy.dependancy import admin

router=APIRouter()

@router.post("/")
def assigntask(task:TaskCreate,current_user:dict = admin):
    try:
        assignTask(task=task)
        return {"message":"Done"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))