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


def get_booking(userid):
    sql = f"select attractionId from booking where userid like '{userid}'"
    mycursor.execute(sql)
    attractionId = mycursor.fetchone()
    if attractionId != None:
        attractionId = attractionId[0]
    else:
        return False

    hasBeenBooking = check_booking(userid)
    if hasBeenBooking == True:
        sql = f"select booking.date, booking.time, booking.price, attractions.id, attractions.name, attractions. address, attractions.images from booking inner join attractions on attractions.id = '{attractionId}'"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        return data[0]
    else:
        return False


def update_booking(attractionId, date, time, price, usersId):
    sql = f"update booking set attractionId='{attractionId}', date='{date}', time='{time}', price='{price}' where userId='{usersId}'"
    mycursor.execute(sql)
    mydb.commit()
    mycursor.fetchone()
    if mycursor.rowcount == 1:
        return True
    return False


def check_booking(userid):
    sql = f"select id from booking where userid like '{userid}'"
    mycursor.execute(sql)
    mycursor.fetchone()
    print(mycursor.rowcount)
    if mycursor.rowcount == 1:
        return True
    else:
        return False


def insert_booking(userid, attractionId, date, time, price):
    hasBeenBooking = False
    hasBeenBooking = check_booking(userid)
    if hasBeenBooking == True:
        return False
    sql = f"insert into booking value (null,'{userid}','{attractionId}','{date}','{time}','{price}' )"
    mycursor.execute(sql)
    mydb.commit()
    if mycursor.rowcount == 1:
        return True


def delete_booking(userid):
    hasBeenBooking = check_booking(userid)
    if hasBeenBooking == True:
        sql = f"delete from booking where userid = {userid}"
        mycursor.execute(sql)
        mydb.commit()
        if mycursor.rowcount == 1:
            return True
        return False
    else:
        return False


class bookingInfo:
    def __init__(self, success, message):
        self.success = success
        self.ok = True
        self.message = message

    def getMessage(self):
        if self.success:
            return {"ok": True}
        else:
            return {"error": True, "message": self.message}
