from src.pydantic_schema.User_pydantic import UserLogin
from src.pydantic_schema.User_log_pydantic import add_log,getlog
from src.Database.session import localSession
from src.Database.db_model import User_table,Task_table,User_log
from src.pydantic_schema.task_pydantic import TaskOut
from fastapi import HTTPException


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

def get_user_id(name:str):
    db = localSession()
    try:
        result = db.query(User_table.id).filter(User_table.name == name).first()
        if result:
            return result[0]
        else:
            raise HTTPException(status_code=400, detail="User not found")
    finally:
        db.close()

def addLog(log: add_log,name:str):
    result=get_user_id(name=name)
    db = localSession()
    try:
        log_data = User_log(user_id=result, **log.dict())
        db.add(log_data)
        db.commit()
        return {"message": "Log added successfully"}
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    finally:
        db.close()
        db.close()

def updatelog(log: add_log,name:str):
    db = localSession()
    id=get_user_id(name=name)
    data = db.query(User_log).filter(User_log.user_id == id).order_by(User_log.idx.desc()).first()
    
    if not data:
        raise HTTPException(status_code=401, detail="There is no previously added log for this ID")
    if log.status:
        data.status = log.status
    if log.logout_time:
        data.logout_time = log.logout_time

    db.commit()
    db.close()
    return {"message": "Log updated successfully"}


def getlog_user(id:int):
    db=localSession()
    data=db.query(User_table.name,User_table.email,User_log.status,User_log.login_time,User_log.logout_time).join(User_log,User_log.user_id==User_table.id).filter(User_log.user_id==id).all()
    db.close()
    if not data:
        raise HTTPException(status_code=401,detail="No log added by User")
    else:
        log_ls=[{
            "User_name":i[0],
            "User_email":i[1],
            "status":i[2],
            "login_time":i[3],
            "logout_time":i[4]
        }
        for i in data
        ]
        return log_ls

