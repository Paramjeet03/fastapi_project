from src.Database.session import localSession
from src.Database.db_model import User_table,Task_table

def report_db():
    db=localSession()
    Total_account=db.query(User_table.email).count()
    Total_user=db.query(User_table.email).filter(User_table.role != "admin").count()
    Total_Done=db.query(Task_table).filter(Task_table.status == "Done").count()
    return {"Total_account :- ":Total_account,"Total_user :- ":Total_user,"Total_admin :- ":Total_account-Total_user,"Total_Done_project :-":Total_Done}
