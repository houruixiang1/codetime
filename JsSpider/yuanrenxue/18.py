import requests
import re
import json
list = []
# for i in range(1,6):

headers = {
    'user-agent': 'yuanrenxue.project',
    'cookie': 'tk=-1084994714126981561; sessionid=wugv1rpvnc70jmosbefecidbrgei44qy;'
}
url = 'https://match.yuanrenxue.com/match/18data?page=1'
resp = requests.get(url=url,headers=headers).json()
# print(resp)
r1 = resp['data']
for j in r1:
    list.append(j['value'])
print(list)



