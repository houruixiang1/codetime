import execjs
import requests
import re



password = 'sAVcxHcesjyZcip6ozvf9g=='
node = execjs.get()
# ctc1 = node.compile(open(r'C:\CodeTime\JsSpider\login\js\天翼云password.js',mode='r',encoding='utf-8').read())
# funcName = 'get_password()'
# password = ctc1.eval(funcName)
# print(password)
ctc = node.compile(open(r'C:\CodeTime\JsSpider\login\js\天翼云login.js',mode='r',encoding='utf-8').read())
funcName1 = 'seqcode()'
funcName2 = 'signature()'
seqcode = ctc.eval(funcName1)
signature = ctc.eval(funcName2)
# print(seqcode,signature)
url = 'https://m.ctyun.cn/account/login?userName=1302897902@qq.com' \
      '&password={}&referrer=wap&mainVersion=300021100' \
      '&comParam_curTime=1637027657789' \
      '&comParam_seqCode={}' \
      '&comParam_signature={}' \
      '&isCheck=true&locale=zh-cn'.format(password,seqcode,signature)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Host': 'm.ctyun.cn',
    'Referer': 'https://m.ctyun.cn/wap/main/auth/login',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive'
}
resp = requests.get(url=url,headers=headers)
print(resp.text)