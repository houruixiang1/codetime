import execjs
import requests
url = 'http://eip.chanfine.com/j_acegi_security_check'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
}
node = execjs.get()
ctc = node.compile(open('C:\CodeTime\js\ChangFang.js',encoding = 'utf-8').read())
funcName = 'getpwd("{0}")'.format('999999')
pwd = ctc.eval(funcName)
data = {
    'j_username': '123@qq.com',
    'j_password': pwd,
    'j_redirectto':''
}
resp = requests.post(url = url,headers=headers,data=data).text
print(resp)