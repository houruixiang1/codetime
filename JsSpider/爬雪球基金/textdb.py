import pymysql

host='localhost'
user='root'
password='123456'
port=3306
try:
    db = pymysql.connect(host=host,user=user,password=password,port=port,db='dbtest')
    print('数据库成功连接!')
    cur = db.cursor()
    cur.execute("DROP TABLE IF EXISTS 雪球基金")
    sql1='INSERT INTo 雪球基金(Name, Email, Age) VALUE (%s,%s,%s)'
    sql2='create table 雪球基金(Name CHAR(20) NOT NULL,Email CHAR(20),Age int)'
    value = ('Mike','123@163.com', 20)
    cur.execute(sql2)
    cur.execute(sql1, value)
    db.commit()
except pymysql.Error as e:
    print("biaoge成功!")
    print("数据插入失败:" + str(e))
db.close()