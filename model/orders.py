import mysql.connector
import os
from dotenv import load_dotenv
from flask import *
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


def insert_order(rid, aid, aname, address, image, date, time, cname, email, phone, price, uId):
    sql = f"insert into orders value(null,'{rid}','{aid}','{aname}','{address}','{image}','{date}','{time}','{cname}','{email}','{phone}','{price}','{uId}')"
    mycursor.execute(sql)
    mydb.commit()
    if mycursor.rowcount == 1:
        return True


def get_order(rid):
    uId = session['id']
    sql = f"select * from orders left join tappays on orders.rid = '{rid}' and tapId =  '{rid}' where orders.rid = '{rid}' and orders.uId = '{uId}';"
    mycursor.execute(sql)
    data = mycursor.fetchone()
    print(data)
    print(mycursor.rowcount)
    if mycursor.rowcount == 1:
        return data
    else:
        return False


class orderInfo:
    def __init__(self, status, recId, message):
        self.status = status
        self.recId = recId
        self.message = message

    def getMessage(self):
        if self.status == 0:
            return {"data": {
                "number": self.recId,
                "payment": {
                    "status": self.status,
                    "message": self.message
                }
            }}
        else:
            return {"error": True, "message": self.message}
