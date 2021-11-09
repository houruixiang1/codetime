import pymysql

host='localhost'
user='root'
password='123456'
port=3306
try:
    db=pymysql.connect(host=host,user=user,password=password,port=port,db='雪球基金')
    print('数据库连接成功！')
except pymysql.Error as e:
    print('数据库连接失败：'+str(e))
cursor=db.cursor()
sql = 'insert into 雪球基金(code,name,price,zde,zdf,nczj,cjl,cje,hsl,ttm,gxl,sz) values (s%,s%,s%,s%,s%,s%,s%,s%,s%,s%,s%,s%)'
# for data in data_dict:
#     print(data)
#     try:
#         print('123')
#         cursor.execute(sql,data_dict)
#         print('执行成功后！')
#         db.commit()
#         print('插入成功！')
#     except:
#         db.rollback()
#         print('插入失败！')