import mysql.connector
from mysql.connector import pooling
import os
from dotenv import load_dotenv
load_dotenv()
# 連線
poolname = "mysqlpool"
poolsize = 3
connectionpool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name=poolname,
    pool_reset_session=True,
    host="localhost",
    user="root",
    password="SERVER_DB_PASSWORD",
    database="SERVER_DB_PASSWORD"
)
mydb = connectionpool.get_connection()
mycursor = mydb.cursor()

# sqlFunction


def insert_tappay(rid, status):
    sql = f"insert into tappays value(null,'{rid}','{status}')"
    mycursor.execute(sql)
    mydb.commit()
    if mycursor.rowcount == 1:
        return True



