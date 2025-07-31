from pydantic import BaseModel
from datetime import datetime

class add_log(BaseModel):
    status:str
    logout_time:datetime



class getlog(BaseModel):
    id:int

class Config:
    from_attributes = True