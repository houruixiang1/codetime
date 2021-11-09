# import pymysql
# datalist = []
# host = 'localhost'
# user = 'root'
# password = '123456'
# db = '雪球基金'
# port = 3306
# try:
#     db = pymysql.connect(host=host, user=user, password=password, port=port, db=db)
#     cursor = db.cursor()
#     sql = "select * from 雪球基金"
#     cursor.execute(sql)
#     for item in cursor.fetchall():
#         datalist.append(item)
#             #print(datalist)
#     db.commit()
#     print('数据取出成功！')
# except pymysql.Error as e:
#     print('数据取出失败：' + str(e))
#     db.rollback()
# db.close()
# print(datalist)

import pymysql
datalist = []
host = 'localhost'
user = 'root'
password = '123456'
db = 'book'
port = 3306
db = pymysql.connect(host=host, user=user, password=password, port=port, db=db)
cur = db.cursor()
sql = 'SELECT t.id,t.sb FROM test t'
cur.execute(sql)
u = cur.fetchall()

# 转换成JSON数据格式
jsonData = {}
xdays = []
yvalues = []

for data in u:
    # xdays.append(str(data[0]))
    xdays.append(data[0])
    yvalues.append(data[1])
print(xdays)
print(yvalues)