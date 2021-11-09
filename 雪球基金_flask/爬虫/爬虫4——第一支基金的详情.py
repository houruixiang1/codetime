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

baseurl="https://xueqiu.com/query/v1/symbol/search/status?u=591622643697049&uuid=1400312241018003456&count=10&comment=0&symbol=SH601919&hl=0&source=user&sort=alpha&page="
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}

for i in range(1, 11):
    url=baseurl+str(i)+'&q=&type=11&session_token=null&access_token=ac3c2b00373aafa819dd63230fff55140e7d0bb4'
    print(url)
    response=requests.get(url=url,headers=headers)
    json_data = response.json()
    pprint.pprint(json_data)
    data_list = json_data['list']
    #print(data_list)
    for data in data_list:
        data_dict = {}
        #print(data)
        data1=data['user']['screen_name'] #评论人名字
        data2=data['title'] #评论专栏
        if data2:
            data2
        else:
            None
        data3=data['timeBefore'] #更新时间
        data4=data['source']  #来源
        data5=data['retweet_count']   #转发量
        if data5:
            if float(data5 > 0):
                data5
            else:
                None
        data6=data['reply_count']   #回答量
        if data6:
            if float(data6 > 0):
                data6
            else:
                None
        data7=data['like_count']  #赞的量
        if data7:
            if float(data7 > 0):
                data7
            else:
                None
        pinglun = data['text']  # 评论
        data8 = (remove_tags(pinglun))

        #print(data1,data2,data3,data4,data5,data6,data7,data8)

        data_dict = {'评论人': data1, '专栏': data2, '更新时间': data3, '来源': data4,
                     '转发量': data5, '回答量': data6,'赞': data7,'评论': data8}
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
                sql = 'insert into 第一支基金详情(name,zhuanlan,update_time,source,zhuanfa,huida,zan)VALUES ("{}","{}","{}","{}","{}","{}","{}")'.format(
                    str(data_dict['评论人']), str(data_dict['专栏']),
                    str(data_dict['更新时间']), str(data_dict['来源']),
                    data_dict['转发量'], data_dict['回答量'],
                    data_dict['赞'])
            cursor.execute(sql)
            db.commit()
            print('数据插入成功！')
        except pymysql.Error as e:
            print('数据插入失败：' + str(e))
            db.rollback()
        db.close()
