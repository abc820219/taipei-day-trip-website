from flask import *
import mysql.connector
# import json
# import re

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="z27089433",
    database="website"
)
mycursor = db.cursor()

# def dropTable(name):
#     sql = f"DROP TABLE {name}"
#     mycursor.execute(sql)
# dropTable("attractions")


# def createAttractionsTable():
#     sql = "create table attractions(pid bigint not null auto_increment primary key comment '流水號',id int not null, name varchar(255) not null comment '景點名稱', category varchar(255) comment '景點分類', description text comment '景點描述', address varchar(255) comment '景點地址', transport text comment '交通方式', mrt varchar(255) comment '捷運', latitude double comment '緯度', longitude double comment '經度', images text comment '圖片')"
#     mycursor.execute(sql)
# createAttractionsTable()

def createUsersTable():
    sql = "create table users(id bigint not null auto_increment primary key comment '流水號', name varchar(255) not null, password varchar(255) not null, email varchar(255) not null)"
    mycursor.execute(sql)


createUsersTable()

# def insertAttractionsSql(i):
#     sql = None
#     if i != None:
#         for i in range(len(file)):
#             if i > 84:
#                 id = file[i]["_id"]
#                 name = file[i]["stitle"]
#                 category = file[i]["CAT2"]
#                 description = file[i]["xbody"]
#                 address = file[i]["address"]
#                 transport = file[i]["info"]
#                 mrt = file[i]["MRT"]
#                 latitude = file[i]["latitude"]
#                 longitude = file[i]["longitude"]
#                 imagesData = file[i]["file"].split('http')
#                 images = []
#                 for image in imagesData:
#                     if(re.search('jpg', image, re.I) != None):
#                         src = f"http{image}"
#                         images = images + [src]
#                 images = json.dumps(images)
#                 sql = f"INSERT INTO attractions VALUES (null,'{id}','{name}','{category}','{description}','{address}','{transport}','{mrt}','{latitude}','{longitude}','{images}')"
#                 mycursor.execute(sql)
#                 db.commit()
#     else:
#         for line in file:
#             id = line["_id"]
#             name = line["stitle"]
#             category = line["CAT2"]
#             description = line["xbody"]
#             address = line["address"]
#             transport = line["info"]
#             mrt = line["MRT"]
#             latitude = line["latitude"]
#             longitude = line["longitude"]
#             imagesData = line["file"].split('http')
#             images = []
#             for image in imagesData:
#                 if(re.search('jpg', image, re.I) != None):
#                     src = f"http{image}"
#                     images = images + [src]
#             images = json.dumps(images)
#             # print(images)
#             sql = f"INSERT INTO attractions VALUES (null,'{id}','{name}','{category}','{description}','{address}','{transport}','{mrt}','{latitude}','{longitude}','{images}')"
#             mycursor.execute(sql)
#             db.commit()

# with open("taipei-attractions.json", mode="r", encoding="utf-8") as file:
#     file = json.load(file)
#     file = file["result"]["results"]
#     insertAttractionsSql(None)
