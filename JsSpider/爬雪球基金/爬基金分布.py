# -*- codeing = utf-8 -*-
import re
from w3lib.html import remove_tags
import requests
import pymysql
import pprint
import csv

# file =open('第一支基金详情.csv',mode='a',encoding='utf-8',newline='')
# csv_write = csv.DictWriter(file,fieldnames=['评论人','专栏','更新时间','来源','转发量','回答量','赞','评论'])
#
# csv_write.writeheader()

url="https://www.amac.org.cn//portal/front/pri/priFundData/getPriFundData?timeType=1&productType=1"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}

response=requests.get(url=url,headers=headers)
json_data = response.json()
pprint.pprint(json_data)
data_list = json_data['data']['data']['fundResult']['dataList']
print(data_list)
for data in data_list:
    data_dict = {}
    #print(data)

    data1=data['areaName'] #评论专栏
    data2=data['custodianNum'] #更新时间
    data3=data['manageFundNum']  #来源
    data4=data['manageFundScale']   #转发量

    #print(data1,data2,data3,data4)

    data_dict = {'辖区名称': data1, '私募基金管理人数量（家）': data2, '管理基金数量（只）': data3,
                     '管理基金规模（亿元）': data4}
    #csv_write.writerow(data_dict)
    host = 'localhost'
    user = 'root'
    password = '123456'
    db = '雪球基金'
    port = 3306
    try:
        db = pymysql.connect(host=host, user=user, password=password, port=port, db=db)
        cursor = db.cursor()
        for data in (data_dict):
            # print(data)
            sql = 'insert into 基金分布(name,usernum,fundnum,scale)VALUES ("{}","{}","{}","{}")'.format(
                str(data_dict['辖区名称']),data_dict['私募基金管理人数量（家）'],
                data_dict['管理基金数量（只）'],data_dict['管理基金规模（亿元）'])
        cursor.execute(sql)
        db.commit()
        print('数据插入成功！')
    except pymysql.Error as e:
        print('数据插入失败：' + str(e))
        db.rollback()
    db.close()
