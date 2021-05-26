from model import *
from flask import *
import urllib.request as req
ordersApp = Blueprint('ordersApp', __name__)


@ordersApp.route('/api/orders', methods=['POST'])
def insertOrdersHandler():
    data = request.get_json()
    prime = data['prime']
    
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
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
            'x-api-key': 'partner_SDmf75bmU83MLWX6HonFPCsCFnXDNEoutXEwtqjdxWzMGP8Q2UfCx9GI'
        }, data=json.dumps(requestData).encode("utf-8"))

    with req.urlopen(resp) as response:
        result = response.read().decode("utf-8")
    print(result)
    return result


# @ordersApp.route("/api/orders")
# def getOrdersHandler():
