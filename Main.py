from fastapi import FastAPI
from src.api.Admin_api import Welcome,login,createAccount,update,report,deleteAccount,readAccount
from src.api.Task_crud_api import taskAssign,taskUpdate,seeTask
from src.api.log_api import setLog,getLogadmin,getlogUser,updateLog

app=FastAPI()
app.include_router(Welcome.router,prefix="/Welcome",tags=["Welcome"])
app.include_router(login.router,prefix="/login",tags=["Login"])
app.include_router(createAccount.router,prefix="/Admin/createAccount",tags=["Account CRUD"])
app.include_router(update.router,prefix="/Admin/updateAccount",tags=["Account CRUD"])
app.include_router(deleteAccount.router,prefix="/Admin/deleteAccount",tags=["Account CRUD"])
app.include_router(readAccount.router,prefix="/User_Admin/seeAccount",tags=["Account CRUD"])
app.include_router(taskAssign.router,prefix="/Admin/assignTask",tags=["Task Assign"])
app.include_router(taskUpdate.router,prefix="/Admin/taskUpdate",tags=["Task Updation"])
app.include_router(seeTask.router,prefix="/User/seeTask",tags=["See Task"])
app.include_router(setLog.router,prefix="/User/addLog",tags=["Add Log"])
app.include_router(getLogadmin.router,prefix="/Admin/getLog",tags=["See log (admin)"])
app.include_router(getlogUser.router,prefix="/User/getLog",tags=["See log (User)"])
app.include_router(updateLog.router,prefix="/User/updateLog",tags=["Log Update"])
app.include_router(report.router,prefix="/totalReport",tags=["Report"])
