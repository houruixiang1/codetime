import requests
from concurrent.futures import ThreadPoolExecutor
from lxml import etree
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
}
f =open("data.csv", mode='w',newline="", encoding="utf-8")
csvwrites = csv.writer(f)

def Page_one_data(url):
    data = {
        "limit": 20,
        "current": i,
        "pubDateStartTime": '',
        "pubDateEndTime": '',
        "prodPcatid": '',
        "prodCatid": '',
        "prodName": '',
    }
    resp = requests.post(url=url,headers=headers,data=data)
    lists = resp.json()['list']
    for list in lists:
        name = list['prodName']
        id = list['id']
        prod_id = list['prodCatid']
        prodCat = list['prodCat']
        place = list['place']
        pubdate = list['pubDate']
        csvwrites.writerow([name, id, prod_id, prodCat, place, pubdate])
        print(name,"提取完毕")

if __name__ == '__main__':
    # for i in range(1,201):
    #     a= Page_one_data('http://www.xinfadi.com.cn/getPriceData.html',i)
    #     print("提取完毕！！！")
    #     break
    with ThreadPoolExecutor(50) as t:
        for i in range(1,201):
            t.submit(Page_one_data,'http://www.xinfadi.com.cn/getPriceData.html')
        print("下载完毕！！！！")