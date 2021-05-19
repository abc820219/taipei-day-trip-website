from model import *
from flask import *
usersApp = Blueprint('usersApp', __name__)


@usersApp.route("/api/user", methods=["POST"])
def loginHandler():
    data = request.get_json()
    email = data['email']
    password = data['password']
    canLogin = False
    canLogin = check_account(email, password)
    if canLogin != False:
        session.permanent = True
        session["id"] = canLogin
    result = json.dumps(registerLoginLogoutInfo(canLogin, "登入失敗").getMessage())
    print(session)
    return result


@ usersApp.route("/api/user", methods=["PATCH"])
def registerLoginHandler():
    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']
    if not name or not email or not password:
        return registerLoginLogoutInfo(False, "請輸入正確資料").getMessage()
    registerFlag = register_user(name, email, password)

    if registerFlag == "信箱重複":
        return registerLoginLogoutInfo(False, "信箱重複").getMessage()

    # print(register_user(name, email, password))
    if registerFlag == True:
        return registerLoginLogoutInfo(True, "註冊成功").getMessage()
    else:
        return registerLoginLogoutInfo(False, "註冊失敗").getMessage()


@usersApp.route("/api/user", methods=["GET"])
def checkUserIsLogin():
    if "id" in session:
        result = {}
        id = session["id"]
        userData = get_user(id)
        result['id'] = userData[0]
        result['name'] = userData[1]
        result['email'] = userData[3]
        return json.dumps(result)
    else:
        return json.dumps(None)


@usersApp.route("/api/user", methods=["DELETE"])
def logoutHandler():    
    session.clear()
    return json.dumps(True)
