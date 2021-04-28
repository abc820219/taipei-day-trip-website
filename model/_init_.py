import mysql.connector
# 連線
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="z27089433",
    database="website"
)
mycursor = mydb.cursor()

# sqlFunction


def get_attractions_count(keyword):
    if keyword:
        sql = f"select count(*) from attractions where name like '%{keyword}%'"
    else:
        sql = f"select count(*) from attractions"
    mycursor.execute(sql)
    return mycursor.fetchone()[0]


def get_attractions_list(startPage, perpage, keyword):
    if keyword:
        sql = f"select * from attractions where name like '%{keyword}%' limit   {startPage}, {perpage}"
    else:
        sql = f"select * from attractions limit {startPage}, {perpage}"
    mycursor.execute(sql)
    return mycursor.fetchall()


def get_attraction(id):
    sql = f"select * from attractions where id like '{attractionId}'"
    mycursor.execute(sql)
    return mycursor.fetchone()
    # dataClass


class AttractionsRow:
    def __init__(self, pid, id, name, category, description, address, transport, mrt, latitude, longitude, images):
        self.pid = pid
        self.id = id
        self.name = name
        self.category = category
        self.description = description
        self.address = address
        self.transport = transport
        self.mrt = mrt
        self.latitude = latitude
        self.longitude = longitude
        self.images = images

    def getData(self):
        rowData = {}
        rowData["pid"] = self.pid
        rowData["id"] = self.id
        rowData["name"] = self.name
        rowData["category"] = self.category
        rowData["description"] = self.description
        rowData["address"] = self.address
        rowData["transport"] = self.transport
        rowData["mrt"] = self.mrt
        rowData["latitude"] = self.latitude
        rowData["longitude"] = self.longitude
        rowData["images"] = self.images
        return rowData
