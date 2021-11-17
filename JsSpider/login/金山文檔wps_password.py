import requests
import execjs
# pwd = '12345678'
node = execjs.get()
ctc = node.compile(open(r'C:\CodeTime\JsSpider\login\js\金山文檔wps_password.js',mode='r',encoding='utf-8').read())
funcName = 'get_pwd()'
password = ctc.eval(funcName)
print(password)
# data= {
# 'return_url': 'https://www.jisilu.cn/account/find_password/modify/mobile_1__key-fe6b60ab8dcd02a49a75',
# 'user_name': username,
# 'password': password,
# 'net_auto_login': 1,
# '_post_type': 'ajax',
# 'aes': 1
# }
# resp = requests.post('https://www.jisilu.cn/account/ajax/login_process/',data=data)
# print(resp.cookies)