import time

import requests
from bs4 import BeautifulSoup
import os


url ="https://www.umei.cc/bizhitupian/keaibizhi/dongman.htm"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'

}

if not os.path.exists("./uimei/"):
    os.mkdir("./uimei/")

response = requests.get(url=url,headers=headers)
response.encoding='utf-8'
# print(response.text)

bs = BeautifulSoup(response.text,'html.parser')
result1 = bs.find("div",class_="TypeList")
# print(result1)
result2 = result1.findAll("a",class_="TypeBigPics")
# print(result2)
for result in result2:
    detail_url = result.get('href')
    urls = "https://www.umei.cc" +detail_url
    # print(urls)
    response1 = requests.get(url=urls,headers=headers)
    response1.encoding='utf-8'
    # print(response1.text)
    bs1 = BeautifulSoup(response1.text,'html.parser')
    result5 = bs1.find("div",class_="ArticleTitle")
    file_name = result5.text
    # print(file_name)
    result3 = bs1.find("div",class_="ImageBody").find_all('img')
    # print(result3)
    for result4 in result3:
        download_url = result4.get('src')
        # print(download_url)
        with open("./uimei/"+file_name+'.jpg',mode="wb") as f:
            result6 = requests.get(url=download_url,headers=headers).content
            f.write(result6)
        time.sleep(1)
    print("下载结束",file_name)
print("全部下载结束")


