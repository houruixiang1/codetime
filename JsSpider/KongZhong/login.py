# js反混淆，需要在谷歌浏览器中进行配置
# 开发者工具--setting--source--勾选第一项（最好这个目录下全部勾选，我所看的博主是全部勾选的）
import re
import time

import execjs
import requests

password = ''
timestamp = str(int(time.time()*1000))

url_1 = 'https://sso.kongzhong.com/ajaxLogin?j=j&jsonp=j&service=https://passport.kongzhong.com/&_={}'.format(timestamp)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Referer': 'https://passport.kongzhong.com/'
}
response = requests.get(url=url_1,headers=headers).text
dc = re.search('"dc":"(.*?)"',response,re.S).group(1).strip()
# print(response)
node = execjs.get()
ctc = node.compile(open('C:\CodeTime\js\KongZhong.js',encoding = 'utf-8').read())
funcName = 'getpassword("{0}","{1}")'.format('123456',dc)
pwd = ctc.eval(funcName)
# print(pwd)
url = 'https://sso.kongzhong.com/ajaxLogin?j=j&&type=1&service=https://passport.kongzhong.com/&username=123%40qq.com&password={}&vcode=&toSave=0&_={}'.format(pwd,timestamp)
resp = requests.get(url=url,headers=headers).text
print(resp)
