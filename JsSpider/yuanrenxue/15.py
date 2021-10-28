import requests
import pywasm
import json
import time
import random

t1 = int(int(time.time()*1000)/1000/2)
t2 = t1 - int(random.random()*50) +1
# print(t1,t2)
vm = pywasm.load(r"D:\pycharmproject\main.wasm")
result = vm.exec("encode",[t1, t2])
m = str(result) + '|' + str(t1) + '|' + str(t2)
list = []
for i in range(1,6):
    url = 'https://match.yuanrenxue.com/api/match/15?m={}&page={}'.format(m,i)
    headers = {
        'user-agent': 'yuanrenxue.project',
        'cookie': 'sessionid=zgm0rlsvh3lgtakbwshm3tolg7ompi53;',
        'Referer': 'https://match.yuanrenxue.com/match/15'
    }
    resp = requests.get(url = url,headers=headers).json()
    for j in resp['data']:
        list.append(j['value'])
print(list)
a = sum(list)
print(a)


