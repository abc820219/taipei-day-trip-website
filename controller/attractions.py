from model import *
from flask import *
import math
attractionApp = Blueprint('attractionApp', __name__)

@attractionApp.route("/api/attractions")
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



@attractionApp.route("/api/attraction/<attractionId>")
def attractionHandler(attractionId):
    data = get_attraction(attractionId)
    print(data)
    rowData = AttractionsRow(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10])
    result = rowData.getData()
    return json.dumps(result)