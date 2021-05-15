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
    if canLogin == True:
        session.permanent = True
        session["email"] = email
    result = json.dumps(registerLoginLogoutInfo(canLogin, "登入失敗").getMessage())
    return result


@ usersApp.route("/api/user", methods=["PATCH"])
def registerLoginHandler():
    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']
    if register_user(name, email, password) == True:
        return registerLoginLogoutInfo(True, "註冊成功").getMessage()
    else:
        return registerLoginLogoutInfo(False, "註冊失敗").getMessage()


@usersApp.route("/api/user", methods=["GET"])
def checkUserIsLogin():
    if "email" in session:
        return json.dumps(True)
    else:
        return json.dumps(None)


@usersApp.route("/api/user", methods=["DELETE"])
def logoutHandler():
    session.pop("email", None)
    return json.dumps(True)
