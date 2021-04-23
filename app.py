from flask import *
import math
import mysql.connector
# 連線
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="website"
)
mycursor = mydb.cursor()

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Pages


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/attraction/<id>")
def attraction(id):
    return render_template("attraction.html")


@app.route("/booking")
def booking():
    return render_template("booking.html")


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

# API
@app.route("/api/attractions")
def getAttractionsHandler():
    keyword = request.args.get('keyword')
    page = int(request.args.get('page'))
    if keyword:
        sql = f"select count(*) from attractions where name like '%{keyword}%'"
    else:
        sql = f"select count(*) from attractions"

    mycursor.execute(sql)
    perpage = 12
    totalPage = mycursor.fetchone()[0]
    lastPage = math.floor(totalPage / perpage)
    startPage = perpage * page

    if page > lastPage:
        startPage = 0

    if keyword:
        sql = f"select * from attractions where name like '%{keyword}%' limit {startPage}, {perpage}"
    else:
        sql = f"select * from attractions limit {startPage}, {perpage}"

    mycursor.execute(sql)
    data = mycursor.fetchall()
    nextPage = page + 1

    if nextPage > lastPage:
        nextPage = 0

    result = {}
    result['data'] = []
    result['page'] = nextPage

    for i in range(len(data)):
        rowData = {}
        rowData['pid'] = data[i][0]
        rowData['id'] = data[i][1]
        rowData['name'] = data[i][2]
        rowData['category'] = data[i][3]
        rowData['description'] = data[i][4]
        rowData['address'] = data[i][5]
        rowData['transport'] = data[i][6]
        rowData['mrt'] = data[i][7]
        rowData['latitude'] = data[i][8]
        rowData['longitude'] = data[i][9]
        rowData['images'] = data[i][10]
        result['data'].insert(i, rowData)

    return result


@app.route("/api/attraction/<attractionId>")
def attractionHandler(attractionId):
    sql = f"select * from attractions where id like '{attractionId}'"
    mycursor.execute(sql)
    result = mycursor.fetchone()
    return json.dumps(result)

app.run(port=3000)
