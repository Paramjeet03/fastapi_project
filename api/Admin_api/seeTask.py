from fastapi import APIRouter
from src.CRUD.User_crud import getTask
from src.pydantic_schema.task_pydantic import TaskOut
from src.Dependancy.dependancy import both

router=APIRouter()

@router.post("/")
def get_Task(out:TaskOut,current_user: dict =both):
    return getTask(out=out)

    