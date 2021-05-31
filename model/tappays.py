import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()
# 連線
mydb = mysql.connector.connect(
    host=os.getenv("SERVER_DB_HOST"),
    user=os.getenv("SERVER_DB_USER"),
    password=os.getenv("SERVER_DB_PASSWORD"),
    database=os.getenv("SERVER_DB_DATABASE")
)
mycursor = mydb.cursor()

# sqlFunction


def insert_tappay(rid, status):
    sql = f"insert into tappays value(null,'{rid}','{status}')"
    mycursor.execute(sql)
    mydb.commit()
    if mycursor.rowcount == 1:
        return True



