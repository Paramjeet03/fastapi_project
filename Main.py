from fastapi import FastAPI
from src.api.Admin_api import login,createAccount,update,taskAssign,taskUpdate,seeTask,setLog

app=FastAPI()
app.include_router(login.router,prefix="/login",tags=["Login"])
app.include_router(createAccount.router,prefix="/Admin/createAccount",tags=["Create New Account"])
app.include_router(update.router,prefix="/Admin/updateAccount",tags=["Account Updation"])
app.include_router(taskAssign.router,prefix="/Admin/assignTask",tags=["Task Assign"])
app.include_router(taskUpdate.router,prefix="/Admin/taskUpdate",tags=["Task Updation"])
app.include_router(seeTask.router,prefix="/User/seeTask",tags=["See Task"])
app.include_router(setLog.router,prefix="/User/addLog",tags=["Add Log"])
