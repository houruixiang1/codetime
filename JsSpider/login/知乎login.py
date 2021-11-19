import hmac
import time
import execjs
import hashlib

# timestamp = str(int(time.time()*1000))
# print(timestamp)
ha = hmac.new(b'd1b964811afb40118a12068ff74a12f4', digestmod=hashlib.sha1)
grant_type = "password"
client_id = 'c3cef7c66a1843f8b3a9e6a1e3160e20'
source = 'com.zhihu.web'
timestamp = '1637228784061'
ha.update(bytes((grant_type + client_id + source + timestamp), 'utf-8'))
signature = ha.hexdigest()
print(signature)
node = execjs.get()
ctc = node.compile(open(r'C:\CodeTime\JsSpider\login\js\知乎login.js',mode='r',encoding='utf-8').read())
funcName = 'get_sign()'
sign = ctc.eval(funcName)
print(sign)