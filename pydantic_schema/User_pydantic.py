from pydantic import BaseModel, EmailStr
from datetime import datetime
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str

   

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Update_user(BaseModel):
     email:EmailStr
     role:str = None
     name:str = None




class Config:
    from_attributes = True