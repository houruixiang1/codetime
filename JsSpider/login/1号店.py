import requests
import execjs
import json

node = execjs.get()
ctc = node.compile(open(r'C:\CodeTime\JsSpider\login\js\1号店.js',mode='r',encoding='utf-8').read())
username = 18737540525
pwd = 123456
funcName = 'get_username("{0}","{1}")'.format(username,pwd)
enery = ctc.eval(funcName)
# data = json.load(str(enery))
print(enery)
# enery_username = data[0]
# enery_pwd = data[1]
# print(enery_pwd,enery_username)
