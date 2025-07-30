from src.pydantic_schema.User_pydantic import UserCreate,Update_user
from src.pydantic_schema.task_pydantic import TaskCreate,UpdateTask
from src.Database.session import localSession
from src.Database.db_model import User_table,Task_table
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
        db.close()
        return {"message": "User updated successfully"}
    else:
        raise HTTPException(status_code=400, detail="No values provided for update")
    
def assignTask(task:TaskCreate):
    db=localSession()
    if not db.query(User_table).filter(User_table.id == task.assigned_to).first():
        raise HTTPException(status_code=400,detail="User id not exist !!")
    else:
        data=Task_table(**task.dict())
        db.add(data)
        db.commit()


def updateTask(idx: int, updateTask: UpdateTask):
    db = localSession()
    user_in_db = db.query(Task_table).filter(Task_table.idx == idx).first()
    if not user_in_db:
        raise HTTPException(status_code=400, detail="Task id does not exist")

    updated = False

    if updateTask.assigned_to is not None:
        assigned_user = db.query(User_table).filter(User_table.id == updateTask.assigned_to).first()
        if not assigned_user:
            raise HTTPException(status_code=400, detail="Assigned user does not exist")
        user_in_db.assigned_to = updateTask.assigned_to
        updated = True

    if updateTask.title is not None:
        user_in_db.title = updateTask.title
        updated = True

    if updateTask.description is not None:
        user_in_db.description = updateTask.description
        updated = True

    if updateTask.status is not None:
        user_in_db.status = updateTask.status
        updated = True

    if updated:
        db.commit()
        db.close()
        return {"message": "User Task updated successfully"}
    else:
        raise HTTPException(status_code=400, detail="No values provided for update")


