from model import *
from flask import *
import urllib.request as req
ordersApp = Blueprint('ordersApp', __name__)


@ordersApp.route('/api/orders', methods=['POST'])
def insertOrdersHandler():
    data = request.get_json()
    prime = data['prime']
    price = data['order']['price']
    time = data['order']['trip']['time']
    date = data['order']['trip']['date']
    aid = data['order']['trip']['attraction']['id']
    aname = data['order']['trip']['attraction']['name']
    address = data['order']['trip']['attraction']['address']
    image = data['order']['trip']['attraction']['image']

    cname = data['order']['contact']['name']
    email = data['order']['contact']['email']
    phone = data['order']['contact']['phone']

    uId = session['id']

    url = "https://sandbox.tappaysdk.com/tpc/payment/pay-by-prime"
    requestData = {
        "prime": prime,
        "partner_key": "partner_SDmf75bmU83MLWX6HonFPCsCFnXDNEoutXEwtqjdxWzMGP8Q2UfCx9GI",
        "merchant_id": "HANWEN_TAISHIN",
        "details": "TapPay Test",
        "amount": 100,
        "cardholder": {
            "phone_number": "+886923456789",
            "name": "王小明",
            "email": "LittleMing@Wang.com",
            "zip_code": "100",
            "address": "台北市天龍區芝麻街1號1樓",
            "national_id": "A123456789"
        },
        "remember": False
    }
    resp = req.Request(
        url, headers={
            'Content-Type': 'application/json',
            'x-api-key': 'partner_SDmf75bmU83MLWX6HonFPCsCFnXDNEoutXEwtqjdxWzMGP8Q2UfCx9GI'
        }, data=json.dumps(requestData, ensure_ascii=False).encode("utf-8"))
    with req.urlopen(resp) as response:
        result = response.read().decode("utf-8")
        result = json.loads(result)
        if result['status'] == 0:
            status = result['status']
            recId = result['rec_trade_id']
            isSuccess = insert_tappay(recId, status)
            if isSuccess:
                print(price)
                isSuccess = insert_order(
                    recId, aid, aname, address, image, date, time, cname, email, phone, price,uId)
                if isSuccess:
                    return orderInfo(status, recId, '付款成功').getMessage()
                else:
                    return orderInfo(status, recId, '付款失敗,訂單不成立').getMessage()
            else:
                return orderInfo(status, recId, '付款失敗,訂單不成立').getMessage()
        else:
            return orderInfo(999, "999", '付款失敗,訂單不成立').getMessage()


@ordersApp.route("/api/orders/<orderNumber>")
def getOrdersHandler(orderNumber):
    orderData = get_order(orderNumber)
    print(orderData)
    if orderData != False:
        result = {
            "number": orderData[1],
            "price": orderData[11],
            "trip": {
                "attraction": {
                    "id": orderData[2],
                    "name": orderData[3],
                    "address": orderData[4],
                    "image": orderData[5]
                },
                "date": orderData[6],
                "time": orderData[7]
            },
            "contact": {
                "name": orderData[8],
                "email": orderData[9],
                "phone": orderData[10]
            },
            "status": orderData[15]
        }
        return result
    else:
        return orderInfo(999, "999", '找不到訂單').getMessage()
