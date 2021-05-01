from model import *
from flask import *
from flask_cors import CORS
import math
controllerApp = Blueprint('controllerApp', __name__)
@controllerApp.route("/api/attractions")
def getAttractionsHandler():
    keyword = request.args.get('keyword')
    page = int(request.args.get('page'))
    perpage = 12
    totalPage = get_attractions_count(keyword)
    lastPage = math.floor(totalPage / perpage)
    startPage = perpage * page
    if page > lastPage:
        startPage = 0
    data = get_attractions_list(startPage, perpage, keyword)
    nextPage = page + 1
    if nextPage > lastPage:
        nextPage = None
    result = {}
    result['data'] = []
    result['page'] = nextPage
    for i in range(len(data)):
        rowData = AttractionsRow(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6], data[i][7], data[i][8], data[i][9], data[i][10])
        rowData = rowData.getData()
        result['data'].insert(i, rowData)
    return result
@controllerApp.route("/api/attraction/<attractionId>")
def attractionHandler(attractionId):
    data = get_attraction(attractionId)
    rowData = AttractionsRow(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6], data[i][7], data[i][8], data[i][9], data[i][10])
    return json.dumps(result)
