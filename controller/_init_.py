from model import *
from flask import *
from flask_cors import CORS
import mysql.connector
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.config["TEMPLATES_AUTO_RELOAD"] = True
CORS(app)

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
        nextPage = None

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
    data = mycursor.fetchone()
    result = {}
    result['pid'] = data[0]
    result['id'] = data[1]
    result['name'] = data[2]
    result['category'] = data[3]
    result['description'] = data[4]
    result['address'] = data[5]
    result['transport'] = data[6]
    result['mrt'] = data[7]
    result['latitude'] = data[8]
    result['longitude'] = data[9]
    result['images'] = data[10]
    return json.dumps(result)