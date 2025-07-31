from src.pydantic_schema.User_pydantic import UserLogin,log_detail
from src.Database.session import localSession
from src.Database.db_model import User_table,Task_table,User_log
from src.pydantic_schema.task_pydantic import TaskOut
from fastapi import HTTPException,Depends
from src.Dependancy.dependancy import user


def get_user(login:UserLogin):
    db=localSession()
    data=db.query(User_table).filter(User_table.email==login.email).first()
    db.close()
    return data

def getTask(out: TaskOut):
    db = localSession()
    try:
        user = db.query(User_table).filter(User_table.id == out.id).first()
        if not user:
            raise HTTPException(status_code=400, detail="User ID does not exist!")

        tasks = db.query(Task_table.assigned_to,User_table.name,User_table.email,Task_table.title,Task_table.description,Task_table.status,Task_table.given_on).filter(Task_table.assigned_to == out.id).join(User_table).all()

        if not tasks:
            raise HTTPException(status_code=400, detail="No task assigned to User ID!")

        task_list = [
            {
                "assigned_to": t[0],"name": t[1],"email": t[2],"title": t[3],"description": t[4],"status": t[5],"given_on": t[6],
            }
            for t in tasks
        ]

        return task_list

    finally:
        db.close()

def get_user_id(current_user: dict = user):
    db = localSession()
    try:
        result = db.query(User_table.id).filter(User_table.email == current_user["username"]).first()
        if result:
            return result[0]
        else:
            raise HTTPException(status_code=400, detail="User not found")
    finally:
        db.close()

def addLog(log: log_detail, user_id: int = Depends(get_user_id)):
    db = localSession()
    try:    
        user = db.query(User_table).filter(User_table.id == user_id).first()
        if not user:
            raise HTTPException(status_code=400, detail="User ID does not exist!")
        else:
            log_data = User_log(user_id=user_id, **log.dict())
            db.add(log_data)
            db.commit()
            return {"message": "Log added successfully"}
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    finally:
        db.close()
        db.close()
