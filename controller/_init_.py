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
    perpage = 12
    totalPage = model.get_attractions_count(keyword)
    lastPage = math.floor(totalPage / perpage)
    startPage = perpage * page
    if page > lastPage:
        startPage = 0
    data = model.get_attractions_list(startPage, perpage, keyword)
    nextPage = page + 1
    if nextPage > lastPage:
        nextPage = None
    result = {}
    result['data'] = []
    result['page'] = nextPage
    for i in range(len(data)):
        rowData = model.AttractionsRow(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6], data[i][7], data[i][8], data[i][9], data[i][10])
        result['data'].insert(i, rowData)
    return result


@app.route("/api/attraction/<attractionId>")
def attractionHandler(attractionId):
    data = get_attraction(attractionId)
    rowData = model.AttractionsRow(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6], data[i][7], data[i][8], data[i][9], data[i][10])
    return json.dumps(result)
