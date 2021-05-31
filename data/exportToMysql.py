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


# def createUsersTable():
#     sql = "create table users(id bigint not null auto_increment primary key comment '流水號', name varchar(255) not null, password varchar(255) not null, email varchar(255) not null)"
#     mycursor.execute(sql)
# createUsersTable()


# def createBookingTable():
#     sql = "create table booking(id bigint not null auto_increment primary key comment '流水號', userid int not null comment '使用者id', attractionId int not null comment '景點id', date date not null comment '預約日期', time varchar(255) not null comment '時段', price int not null comment '價錢')"
#     mycursor.execute(sql)

# createBookingTable()


def createTapPays():
    sql = "create table tappays(id bigint not null auto_increment primary key comment '流水號', tapId varchar(255) not null comment '交易識別碼', status int not null comment '狀態碼')"
    mycursor.execute(sql)


createTapPays()


# def createOrders():
#     sql = "create table orders(id bigint not null auto_increment primary key comment '流水號',rid varchar(255) not null comment 'tappayID',aId int not null comment '景點ID', aname varchar(255) not null comment '景點名稱', address varchar(255) not null comment '景點地址', image varchar(255) not null comment '圖片url', date varchar(255) not null comment '景點日期', time varchar(255) not null comment '景點時段', cname varchar(255) not null comment'聯絡人', email varchar(255) not null comment '聯絡人email', phone varchar(255) not null comment '聯絡人電話',price Int not null, uId int not null comment '使用者Id')"
#     mycursor.execute(sql)


# createOrders()


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
