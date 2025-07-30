from fastapi import FastAPI
from src.api.Admin_api import login,createAccount,update

app=FastAPI()
app.include_router(login.router,prefix="/login",tags=["Login"])
app.include_router(createAccount.router,prefix="/Admin/createAccount",tags=["Create New Account"])
app.include_router(update.router,prefix="/Admin/updateAccount",tags=["Account Updation"])