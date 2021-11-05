import json
import re

from lxml import etree
import execjs
import time
from you_get import common
import requests
list3 = []
list=[]
for i in range(1,6):
    get_html_list = []
    timestamp = int(time.time())*1000
    # print(timestamp)
    node = execjs.get()
    ctc = node.compile(open(r'C:\CodeTime\js\6_1.js', encoding='utf-8', mode='r').read())
    funcName1 = 'get_m("{0}")'.format(timestamp)
    # funcName2 = 'get_q("{0}")'.format(timestamp)
    m = ctc.eval(funcName1)
    # q = ctc.eval(funcName2)
    q = '1-'+str(timestamp)+'|'
    # print(m,q)
    data1 = {
        'page':i,
        'm' : m,
        'q' : q
    }
    headers={
        'user-agent':'yuanrenxue.project',
        'cookie':'vaptchaNetway=cn; Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1635232738; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1635761960,1635838280,1635846299,1635903835; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1635471331,1635761963,1635838294,1635903835; no-alert3=true; tk=-1084994714126981561; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1635906545; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1635926356'
    }
    url = 'https://match.yuanrenxue.com/api/match/6?'
    resp = requests.get(url=url,headers=headers,params=data1).json()
    # resp  = json.loads(str(resp))
    # print(type(resp))
    for j in resp['data']:
        get_html_list.append(j)
        list3.append(j['value'])
    # print(list)
    # print(get_html_list)
    node = execjs.get()
    ctc = node.compile(open(r'C:\CodeTime\js\6_2.js', encoding='utf-8', mode='r').read())
    funcName2 = 'get_data("{0}","{1}")'.format(str(get_html_list),1)
    data = ctc.eval(funcName2)
    # print(data)
    prices = re.finditer('<td>(.*?)</td>',data,re.S)
    list1 = []
    for price in prices:
        pr = price.group(1)
        # print(pr)
        list1.append(pr)
    i = 4
    N = 100
    while True:
        list.append(list1[i])
        i = i + 10
        if i >= N:
            break
print(list)
total = 0
for j in range(0,49):
    xyz = list[j]
    total = total + int(xyz)
print(total)