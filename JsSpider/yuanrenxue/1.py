import requests
import execjs
import time


timestamp = int(time.time())*1000
print(timestamp)
node= execjs.get()
ctc = node.compile(open(r'C:\CodeTime\JsSpider\yuanrenxue\1.py',mode='r',encoding='utf-8').read())
funcName = 'get_m()'
m = ctc.eval(funcName)
# print(m)
m = m + '|' + timestamp/1000
print(m)
