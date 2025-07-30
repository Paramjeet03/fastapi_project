from pydantic import BaseModel
class TaskCreate(BaseModel):
    assign_to: int
    title: str
    description: str
    status: str

class TaskOut(TaskCreate):
    id: int

    class Config:
        orm_mode = True