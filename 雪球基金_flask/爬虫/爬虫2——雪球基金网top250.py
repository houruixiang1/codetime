# -*- codeing = utf-8 -*-

import pymysql
import requests
import pprint
import csv
import sqlite3

# file =open('data.csv',mode='a',encoding='utf-8',newline='')
# csv_write = csv.DictWriter(file,fieldnames=['股票代码','股票名称','当前价','涨跌额','涨跌幅','年初至今','成交量','成交额','换手率','市盈率(TTM)','股息率','市值'])
#
# csv_write.writeheader()

url="https://xueqiu.com/service/v5/stock/screener/quote/list?page=1&size=30&order=desc&order_by=amount&exchange=CN&market=CN&type=sha&_=1622644248446"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
response=requests.get(url=url,headers=headers)
json_data = response.json()
pprint.pprint(json_data)

data_list = json_data['data']['list']

for data in data_list:
    data_dict = {}
    #print(data)
    data1=data['symbol']
    data2=data['name']
    data3=data['current']
    data4=data['chg']
    if data4:
        if float(data4>0):
            data4 ="+"+str(data4)
        else:
            data4 =str(data4)
    data5=str(data['percent'])+'%'
    data6=str(data['current_year_percent'])+'%'
    data7=data['volume']
    data8=data['amount']
    data9=str(data['turnover_rate'])+'%'
    data10=data['pe_ttm']
    data11=data['dividend_yield']
    if data11:
        data11 = str(data['dividend_yield'])+'%'
    else:
        None
    data12=data['market_capital']
    #data_dict=(data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12)
    data_dict = {'股票代码':data1,'股票名称':data2,'当前价':data3,'涨跌额':data4,'涨跌幅':data5,'年初至今':data6,'成交量':data7,
                '成交额':data8,'换手率':data9,'市盈率(TTM)':data10,'股息率':data11,'市值':data12}
    #print(data_dict)

    host='localhost'
    user='root'
    password='123456'
    db ='雪球基金'
    port=3306
    try:
        db=pymysql.connect(host=host,user=user,password=password,port=port,db=db)
        cursor = db.cursor()
        for data in (data_dict):
            #print(data)
            sql = 'insert into 雪球基金(code,name, price,zde,zdf,nczj,cjl,cje,hsl,ttm,gxl,sz)VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(
                    data_dict['股票代码'],str(data_dict['股票名称']),
                    data_dict['当前价'],str(data_dict['涨跌额']),
                    str(data_dict['涨跌幅']),str(data_dict['年初至今']),
                    data_dict['成交量'],data_dict['成交额'],
                    str(data_dict['换手率']),data_dict['市盈率(TTM)'],
                    str(data_dict['股息率']),data_dict['市值'])
        cursor.execute(sql)
        db.commit()
        print('数据插入成功！')
    except pymysql.Error as e:
        print('数据插入失败：'+str(e))
        db.rollback()
    db.close()

    #data_dict = {'股票代码':data1,'股票名称':data2,'当前价':data3,'涨跌额':data4,'涨跌幅':data5,'年初至今':data6,'成交量':data7,
    #             '成交额':data8,'换手率':data9,'市盈率(TTM)':data10,'股息率':data11,'市值':data12}
    # csv_write.writerow(data_dict)
# import pymysql
#
#
# class TencentPipeline(object):
#     def __init__(self):
#         # 连接MySQL数据库
#         self.connect = pymysql.connect(host='localhost', user='root', password='123456', db='tencent', port=3306)
#         self.cursor = self.connect.cursor()
#
#     def process_item(self, item, spider):
#         # 往数据库里面写入数据
#         self.cursor.execute(
#             'insert into tencentjob(PostId,jobId, jobName,CountryName,LocationName,BGName,CategoryName,LastUpdateTime,Responsibility,url)VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(
#                 item['PostId'], item['jobId'], pymysql.escape_string(item['jobName']),
#                 pymysql.escape_string(item['CountryName']), pymysql.escape_string(item['LocationName']),
#                 pymysql.escape_string(item['BGName']), pymysql.escape_string(item['CategoryName']),
#                 pymysql.escape_string(item['LastUpdateTime']), pymysql.escape_string(item['Responsibility']),
#                 pymysql.escape_string(item['PostURL'])))
#         self.connect.commit()
#         return item
#
#     # 关闭数据库
#     def close_spider(self, spider):
#         self.cursor.close()
#         self.connect.close()
