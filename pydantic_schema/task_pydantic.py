from pydantic import BaseModel
class TaskCreate(BaseModel):
    assigned_to: int
    title: str
    description: str
    status: str

class UpdateTask(BaseModel):
    assigned_to: int = None
    title: str = None
    description: str = None
    status: str = None

class TaskOut(TaskCreate):
    id: int

    class Config:
        orm_mode = True