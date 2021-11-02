## 未找到对应关系，但思路和过程是正确的（对应关系应该在坐标关系中，即7_1.xml的坐标关系中）
## 动态css，每一次请求有每一次请求的对应关系。

import json
import os
import re

import requests
import base64
from fontTools.ttLib import TTFont
list1 = []
for i in range(1,6):
    url = 'https://match.yuanrenxue.com/api/match/7?page={}'.format(i)
    headers={
        'cookie': 'sessionid=n4k0g3z6q0wo1eedds3krfy6lap1vh1q;',
        'user-agent': 'yuanrenxue.project'
    }
    resp = requests.get(url=url,headers=headers).json()
    # print(resp)

    with open(r'C:\CodeTime\js\7_1.woff','wb')as f:
        f.write(base64.b64decode(resp['woff']))
    font = TTFont(r'C:\CodeTime\js\7_1.woff')
    font.saveXML(r'C:\CodeTime\js\7_1.xml')
    with open(r'C:\CodeTime\js\7_1.xml','r',encoding='utf-8')as f:
        data = f.read()
    # os.remove(r'C:\CodeTime\js\7_1.woff')
    # os.remove(r'C:\CodeTime\js\7_1.xml')
    data1 = re.finditer('<psName name="uni(.*?)"/>',data,re.S)
    list = []
    for da in data1:
        value = da.group(1)
        # print(value)
        list.append(value)
    for i in resp['data']:
        i = json.dumps(i)
        r1 = i.replace('&#x','').strip()
        # print(r1)
        r1 = re.search('value": "(.*?) "',str(r1),re.S).group(1).strip()
        # print(r1)
        r1 = r1.replace(list[0], str(9)).strip()
        r1 = r1.replace(list[1], str(8)).strip()
        r1 = r1.replace(list[2], str(7)).strip()
        r1 = r1.replace(list[3], str(6)).strip()
        r1 = r1.replace(list[4], str(5)).strip()
        r1 = r1.replace(list[5], str(4)).strip()
        r1 = r1.replace(list[6], str(3)).strip()
        r1 = r1.replace(list[7], str(2)).strip()
        r1 = r1.replace(list[8], str(1)).strip()
        r1 = r1.replace(list[9], str(0)).strip()
        r1 = r1.replace(' ','').strip()
        # print(r1)
        list1.append(r1)
start_url = 'https://match.yuanrenxue.com/match/7'
response = requests.get(url=start_url,headers=headers).text
# print(response)
name_list = re.search("荕',(.*?),'狂卩",response,re.S).group(1).strip()
# print(len(list1))
name_list = name_list.replace("'",'').strip()
name_list = name_list.split(",")
real_name_list = []
for i in name_list:
    name = i
    real_name_list.append(name)
# print(real_name_list)
dic = dict(map(lambda x,y:[x,y],real_name_list,list1))
# print(len(dic))
# print(max(dic.values()))
for key,value in dic.items():
    if(value == max(dic.values())):
        print(key,value)







