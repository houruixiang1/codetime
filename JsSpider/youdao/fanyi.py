import random

import requests
import time
import execjs
n= input('请输入一个单词：')
url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
i = str(int(time.time()*1000))
headers = {
    # 'Accept': 'application/json, text/javascript, */*; q=0.01',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '241',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=-1476829725@10.169.0.82; JSESSIONID=aaaYk73MpuJyG-MeTz6Yx; OUTFOX_SEARCH_USER_ID_NCOO=315285074.6367838; fanyi-ad-id=118539; fanyi-ad-closed=1; ___rl__test__cookies={}'.format(i),
    # 'Host': 'fanyi.youdao.com',
    # 'Origin': 'https://fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/',
    # 'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': "Windows",
    # 'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
}
b = '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'

ts = i + str(int(random.random()*10))
# print(ts)
si = "fanyideskweb" + n + ts + "Y2FYu%TNSbMCxc3t2u^XT"
print(si)
node = execjs.get()
ctc = node.compile(open('C:\CodeTime\js\youdaofanyi.js',encoding='utf-8').read())
funcName1 = 'md5("{0}")'.format(b)
bv = ctc.eval(funcName1)
funcName2 = 'md5("{0}")'.format(si)
sign = ctc.eval(funcName2)
print(bv,sign,ts,i)
data = {
    'i': n,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': ts,
    'sign': sign,
    'lts': i,
    'bv': bv,
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}
resp = requests.post(url=url,headers=headers,data=data).text
print(resp)



