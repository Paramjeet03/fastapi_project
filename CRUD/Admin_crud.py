from src.pydantic_schema.User_pydantic import UserCreate,Update_user
from src.Database.session import localSession
from src.Database.db_model import User_table
from src.Auth.Hashing_token import hash_pass
from fastapi import HTTPException

def new_User(user:UserCreate):
        db=localSession()
        if db.query(User_table).filter(User_table.email == user.email).first():
            raise HTTPException(status_code=400,detail="User already registered")
        db.add(User_table(name=user.name, email=user.email, pass_hash=hash_pass(user.password), role=user.role))
        db.commit()
        db.close()
        

def Update_user_table(user: Update_user):
    db=localSession()
    user_in_db = db.query(User_table).filter(User_table.email == user.email).first()
    if not user_in_db:
        raise HTTPException(status_code=400, detail="User does not exist")

    updated = False

    if user.role is not None:
        user_in_db.role = user.role
        updated = True

    if user.name is not None:
        user_in_db.name = user.name
        updated = True

    if updated:
        db.commit()
        return {"message": "User updated successfully"}
    else:
        raise HTTPException(status_code=400, detail="No values provided for update")
