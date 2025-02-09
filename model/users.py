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
    host=os.getenv("SERVER_DB_HOST"),
    user=os.getenv("SERVER_DB_USER"),
    password=os.getenv("SERVER_DB_PASSWORD"),
    database=os.getenv("SERVER_DB_DATABASE")
)
mydb = connectionpool.get_connection()
mycursor = mydb.cursor()


def get_user(id):
    sql = f"SELECT * from users WHERE id like '{id}'"
    mycursor.execute(sql)
    return mycursor.fetchone()


def check_account(email, password):
    sql = f"SELECT id FROM users WHERE email like '{email}' AND password like '{password}'"
    mycursor.execute(sql)
    userId = mycursor.fetchone()
    if userId != None:
            return userId[0]
    else:
            return False


def insert_user(name, email, password):
    isSucceeded = False
    sql = f"insert into users value(null,'{name}','{password}','{email}')"
    mycursor.execute(sql)
    mydb.commit()
    if mycursor.rowcount == 1:
        isSucceeded = True
    return isSucceeded


def register_user(name, email, password):
    isRegistered = check_account(email, password)
    if isRegistered:
        return "信箱重複"
    else:
        isRegistered = insert_user(name, email, password)
        return isRegistered


class registerLoginLogoutInfo:
    def __init__(self, success, message):
        self.success = success
        self.ok = True
        self.message = message

    def getMessage(self):
        if self.success:
            return {"ok": True}
        else:
            return {"error": True, "message": self.message}


class userData:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def getuser(self):
        data = {}
        data["id"] = self.id
        data["name"] = self.name
        data["email"] = self.email
        return data
