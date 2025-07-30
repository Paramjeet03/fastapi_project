from src.pydantic_schema.User_pydantic import UserLogin
from src.Database.session import localSession
from src.Database.db_model import User_table

def get_user(login:UserLogin):
    db=localSession()
    data=db.query(User_table).filter(User_table.email==login.email).first()
    db.close()
    return data
