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


def get_user(id):
    sql = f"SELECT * from users WHERE id like '{id}'"
    mycursor.execute(sql)
    return mycursor.fetchone()


def check_account(email, password):
    sql = f"SELECT count('id') FROM users WHERE email like '{email}' AND password like '{password}'"
    mycursor.execute(sql)
    for user in mycursor:
        if user[0] != 0:
            print(user)
            return user[1]
        else:
            return False


def insert_user(name, email, password):
    isSucceeded = False
    sql = f"insert into users value(null,'{name}','{password}','{email}')"
    mycursor.execute(sql)
    mydb.commit()
    isSucceeded = check_account(email, password)
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
