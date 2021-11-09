import requests
from lxml import etree
import os

url = 'https://www.huya.com/g/lol'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

if not os.path.exists('./LOLpic/'):
    os.mkdir('./LoLpic/')

response = requests.get(url,headers)
# print(response.text)
LoL = etree.HTML(response.content)
Lol = LoL.xpath('//img[@class="pic"]')
for lol in Lol:
    pic_url = lol.xpath('./@data-original')[0]
    anchor = lol.xpath('./@alt')[0]
    # pic_url = pic_url.split('?')[0]
    if 'https:' in pic_url:
        pic_url = pic_url.split('?')[0]
    else:
        pic_url = 'https:'+pic_url.split('?')[0]
    print(pic_url)
    response = requests.get(pic_url,headers)

    with open('./LOLpic/'+anchor+'.jpg','wb')as f:
        f.write(response.content)
    print("图片下载成功...%s"%anchor)

