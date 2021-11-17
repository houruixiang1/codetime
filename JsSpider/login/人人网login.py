import requests
import hashlib
import time

import execjs
# # pwd = '12345678'
#
# node = execjs.get()
# ctc = node.compile(open(r'C:\CodeTime\JsSpider\login\js\人人網.js',mode='r',encoding='utf-8').read())
# funcName = 'get_sig()'
# sig = ctc.eval(funcName)
# print(sig)
# url = 'https://rrwapi.renren.com/account/v1/loginByPassword'
# sign = 'appKey=bcceb522717c2c49f895b561fa913d10callId=1637144573357password=f2200fe4ae83f888fe8293e99c4f8afcsessionKey=user=18737540525bcceb522717c2c49f895b561fa913d10'
# md5 = hashlib.md5()
# md5.update(sign.encode('UTF-8'))
# sign = md5.hexdigest()
# print(sign)
# ctx = execjs.compile(jsinfo, cwd=r"C:\clip-spider-v2\node_modules")
# pwd = ctx.call('get_pwd')
# print(pwd)
session = requests.session()
username = '18737540525'
passwd = '123456'
# with open(file = r"C:\CodeTime\JsSpider\login\人人网login.py",mode = "r",encoding="utf-8") as f:
#     ctx = execjs.compile(f.read())
t = str(int(time.time()*1000))
# sig = ctx.call("getSig",username,passwd,t)
jsinfo = '''
     var CryptoJS = require('crypto-js');
function getSig(username,password,t) {
  newstr = "appKey=bcceb522717c2c49f895b561fa913d10callId=" + t + "password=" + CryptoJS.MD5(password) + "sessionKey=user=" + username + "bcceb522717c2c49f895b561fa913d10"
  // console.log(newstr);
  sign = CryptoJS.MD5(newstr);
  return sign.toString();
}
'''
ctx = execjs.compile(jsinfo, cwd=r"C:\clip-spider-v2\node_modules")
sig = ctx.call("getSig",username,passwd,t)
# print(sig)
data = {
    "appKey":"bcceb522717c2c49f895b561fa913d10",
    "callId": t,
    "password": 'e10adc3949ba59abbe56e057f20f883e',
    "sessionKey":"",
    "sig":sig,
    "user":username
}
# print(data)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67",
    "Content-Type": "application/json;charset=UTF-8",
    "Host": "rrwapi.renren.com",
    "Referer": "https://renren.com/",
}
url = "https://rrwapi.renren.com/account/v1/loginByPassword"
res = session.post(headers=headers,json=data,url=url)
print(res.json())
# if res.json()['errorMsg'] == "成功":
#     print("登录成功")
#     uid = res.json()['data']['uid']
#     sessionKey = res.json()['data']['sessionKey']
#     secretKey = res.json()['data']['secretKey']
#     return uid,sessionKey,secretKey