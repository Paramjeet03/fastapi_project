from pydantic import BaseModel
from datetime import datetime

class add_log(BaseModel):
    status:str
    logout_time:datetime


class updateLog(add_log):
    id:int

class getlog(BaseModel):
    id:int

class Config:
    from_attributes = True