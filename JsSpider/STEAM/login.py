import requests
# import re
import time
import execjs


timestamp = str(int(time.time()*1000))
# print(timestamp)
url_1 = 'https://store.steampowered.com/login/getrsakey/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

data = {
    'donotcache': timestamp,
    'username': '123@qq.com'
}

resp = requests.post(url=url_1,headers=headers,data=data).json()
# print(resp)
exp = resp['publickey_exp']
mod = resp['publickey_mod']
timestm = resp['timestamp']

node = execjs.get()
ctc = node.compile(open('C:\CodeTime\js\STEAM.js',encoding='utf-8').read())
funcName = 'getpwd("{0}","{1}","{2}")'.format('12345678',mod,exp)
password = ctc.eval(funcName)
# print(password)
url_2 = 'https://store.steampowered.com/login/dologin/'
params = {
    'donotcache': timestamp,
    'password': password,
    'username': '123@qq.com',
    'twofactorcode': '',
    'emailauth': '',
    'loginfriendlyname': '',
    'captchagid': -1,
    'captcha_text': '',
    'emailsteamid': '',
    'rsatimestamp': timestm,
    'remember_login': 'false'
}
response = requests.post(url=url_2,headers=headers,data=params).text
print(response)