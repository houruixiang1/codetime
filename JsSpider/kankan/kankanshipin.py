# 思路没啥问题，扣的js代码有些问题，可以输出sign，但不是真正的sign

import time
import execjs
import requests
import re

start_url = 'http://www.kankanews.com/a/2021-10-30/0039927603.shtml'
resp = requests.get(url=start_url).text
omsid = re.findall('omsid="(.*?)"',resp,re.S)[0]

node = execjs.get()
ctc = node.compile(open('C:\CodeTime\js\kankanshipin.js',encoding = 'utf--8',mode='r').read())
funcName1 = 'get_nonce()'
timestamp = int(time.time())
data= ctc.eval(funcName1)
nonce = 'cd7vn6m6'
timestamp = '1635755423'
# print(data)
# print(timestamp)
data = "nonce={}&platform=pc&timestamp={}&version=1.0&".format(nonce,timestamp)
print(data)
funcName2 = 'get_sign("{0}")'.format(data)
sign = ctc.eval(funcName2)
# print(sign)
url = 'https://api-app.kankanews.com/kankan/pc/getvideo?' \
      'nonce={}&omsid={}&platform=pc&' \
      'timestamp={}&version=1.0&sign={}'.format(nonce,omsid,timestamp,sign)
print(url)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}
response = requests.get(url,headers=headers).text
print(response)