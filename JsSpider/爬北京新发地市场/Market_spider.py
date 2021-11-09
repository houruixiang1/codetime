import requests
import csv

url ='http://www.xinfadi.com.cn/getPriceData.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

response = requests.post(url=url,headers=headers)
data_json = response.json()
f=open('./菜价.csv',mode='w',encoding='utf-8')
csvwrite = csv.writer(f)
lists = data_json['list']
data_dic=[]
for list in lists:
    name =list['prodName']
    id = list['id']
    prod_id = list['prodCatid']
    prodCat = list['prodCat']
    place = list['place']
    pubdate = list['pubDate']
    # data_dic.append(name)
    # data_dic.append(id)
    # print(name,id,prod_id,prodCat,place,pubdate)
    csvwrite.writerow([name,id,prod_id,prodCat,place,pubdate])
print('game over!!!!')





