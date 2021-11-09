import re
import requests
import csv

url = 'https://movie.douban.com/top250?start=0&filter='
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

response = requests.get(url=url,headers=headers)
# print(response.text)

opt = re.compile(r'<div class="info">.*?<span class="title">(?P<name>.*?)</span>'
                 r'.*?<br>.*?/&nbsp;(?P<city>.*?)&nbsp;'
                 r'.*?<span>(?P<num>.*?)人评价</span>'
                 r'.*?<span class="inq">(?P<gen>.*?)</span>',re.S)
iters = opt.finditer(response.text)
f = open('./data.csv',mode='w',encoding='utf-8')
data = csv.writer(f)
for iter in iters:
    # print(iter.group('name'))
    # print(iter.group('city'))
    # print(iter.group('num'))
    # print(iter.group('gen'))
    dic = iter.groupdict()
    data.writerow(dic.values())
print('写入结束')





