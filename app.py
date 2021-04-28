from flask import *
from flask_cors import CORS
import mysql.connector
# 連線
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="z27089433",
    database="website"
)
mycursor = mydb.cursor()

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.config["TEMPLATES_AUTO_RELOAD"] = True
CORS(app)
# Pages


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/attraction/<id>")
def attraction():
    return render_template("attraction.html")


@app.route("/booking")
def booking():
    return render_template("booking.html")


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

from controller import *

# app.run(host="0.0.0.0", port=3000)
app.run(port=3000)
