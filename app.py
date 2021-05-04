from flask import *
from flask_cors import CORS
import mysql.connector
from controller import *
app = Flask(__name__)
app.register_blueprint(controllerApp)
app.config["JSON_AS_ASCII"] = False
app.config["TEMPLATES_AUTO_RELOAD"] = True
# Pages
import os
from dotenv import load_dotenv
load_dotenv()

@app.route("/")
def index():
    return render_template("index.html",title="home")


@app.route("/attraction/<id>")
def attraction(id):
    return render_template("attraction.html",title="detail")


@app.route("/booking")
def booking():
    return render_template("booking.html")


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

if  os.getenv("SERVER_HOST"):
    app.run(host="0.0.0.0", port=3000)
else:
    app.run(port=3000)
