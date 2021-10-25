# 凡科网，点击登录后，会进行图形验证，暂时先不做
import requests
import execjs

url = 'https://i.fkw.com/ajax/login_h.jsp?dogSrc=3'
url_1 = 'https://cv.fkw.com/verify/validate'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Referer': 'https://i.fkw.com/'
}

node = execjs.get()
ctc = node.compile(open(r'C:\CodeTime\js\fkw.js',encoding='utf-8').read())
funcName = 'md5("{0}")'.format('123456')
pwd = ctc.eval(funcName)
print(pwd)
data = {
    'cacct': '123@qq.com',
    'sacct': '',
    'pwd': pwd,
    'autoLogin': 'false',
    'staffLogin': 'false',
    'bizType': 5,
    'dogId': 0,
    'fromsite': 'false',
    'cmd': 'loginCorpNews',
}
resp = requests.post(url = url,headers=headers,data=data).text
print(resp)