from dotenv import load_dotenv
# import os
from flask import *
from flask_cors import CORS
from controller import *
from datetime import timedelta
from controller import *
app = Flask(__name__)
app.register_blueprint(attractionApp)
app.register_blueprint(usersApp)
app.register_blueprint(bookingApp)
app.register_blueprint(ordersApp)
app.config["JSON_AS_ASCII"] = False
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_COOKIE_HTTPONLY"] = False
CORS(app)
# Pages
load_dotenv()
# session密碼
app.secret_key = "hello"
# seesion持續時間
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route("/")
def index():
    return render_template("index.html", title="home")


@app.route("/attraction/<id>")
def attraction(id):
    return render_template("attraction.html", title="detail")


@app.route("/booking")
def booking():
    return render_template("booking.html")


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html",title="thankyou")
# import math


# @app.route("/api/attractions")
# def getAttractionsHandler():
#     keyword = request.args.get('keyword')
#     page = int(request.args.get('page'))
#     perpage = 12
#     totalPage = get_attractions_count(keyword)
#     lastPage = math.floor(totalPage / perpage)
#     startPage = perpage * page
#     if page > lastPage:
#         startPage = 0
#     data = get_attractions_list(startPage, perpage, keyword)
#     nextPage = page + 1
#     if nextPage > lastPage:
#         nextPage = None
#     result = {}
#     result['data'] = []
#     result['page'] = nextPage
#     for i in range(len(data)):
#         rowData = AttractionsRow(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6], data[i][7], data[i][8], data[i][9], data[i][10])
#         rowData = rowData.getData()
#         result['data'].insert(i, rowData)
#     return result


# if os.getenv("SERVER_HOST"):
    app.run(host="0.0.0.0", port=3001)
# else:
#     app.run(port=3001)
