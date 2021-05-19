from model import *
from flask import *
bookingApp = Blueprint('bookingApp', __name__)


@bookingApp.route('/api/booking', methods=['POST'])
def insertBookingHandler():
    data = request.get_json()
    usersid = session["id"]
    attractionId = data["attractionId"]
    date = data["date"]
    time = data["time"]
    price = data["price"]
    isSucceeded = insert_booking(usersid, attractionId, date, time, price)
    if isSucceeded:
        return bookingInfo(True, None).getMessage()
    else:
        return bookingInfo(False, "已有預約,是否覆蓋原本的預約?").getMessage()


@bookingApp.route("/api/booking", methods=["PATCH"])
def updateBookingHandler():
    data = request.get_json()
    attractionId = data["attractionId"]
    date = data["date"]
    time = data["time"]
    price = data["price"]
    isSucceeded = False
    isSucceeded = update_booking(attractionId, date, time, price, session['id'])
    if isSucceeded:
        return bookingInfo(True, None).getMessage()
    else:
        return bookingInfo(False, "更新失敗").getMessage()


@bookingApp.route("/api/booking", methods=["DELETE"])
def delBookingHandler():
    userid = session['id']
    isSuccess = delete_booking(userid)
    return bookingInfo(isSuccess, "取消失敗").getMessage()


@bookingApp.route("/api/booking")
def getBookingHandler():
    userid = session['id']
    bookginData = get_booking(userid)
    if bookginData != False:
        result = {}
        result["attraction"] = {}
        result["attraction"]["id"] = bookginData[3]
        result["attraction"]["name"] = bookginData[4]
        result["attraction"]["address"] = bookginData[5]
        result["attraction"]["images"] = bookginData[6]
        result["date"] = bookginData[0]
        result["time"] = bookginData[1]
        result["price"] = bookginData[2]
        return json.dumps(result)
    else:
        return json.dumps(False)