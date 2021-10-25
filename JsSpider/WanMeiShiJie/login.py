# 分析正确，可能是本地环境胡问题，
# 在发条调试工具中显示出密码加密后的数据，python运行报错，未解决。
import execjs
import requests
import re

url = "https://passport.wanmei.com/sso/login"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

url_1 = 'https://passport.wanmei.com/sso/login?service=passport&isiframe=1&location=2f736166652f'
response = requests.get(url=url_1).text
# print(response)
value = re.search('type="hidden" value="(.*?)"',response,re.S).group(1).strip()
# print(value)
node = execjs.get()
ctc = node.compile(open('C:\CodeTime\js\WanMeiShiJie.js', 'r',encoding='gbk').read())
funcName = 'getPwd("{0}","{1}")'.format('123456',value)
pwd = ctc.eval(funcName)
# ctx = execjs.compile(open('C:\CodeTime\js\WanMeiShiJie.js', 'r', encoding='utf-8').read())
# pwd = ctx.call('getPwd', '123456', value)
# print(pwd)
# data = {
#     'password': pwd,
#     'continue': '',
#     'service': 'passport',
#     'location': '2f736166652f',
#     'needRand': 1,
#     'isiframe': 1,
#     'logintype': 'normal',
#     'CSSStyle': '',
#     'autoLogin': 1,
#     'username': '123@qq.com',
#     'randimg': '4e9ff26d73e54b06a4e8faceb2f3db02;1e33ef5aabe74a8d8f68a1a7d50abfa4',
#     'isAICap': 1
# }
#
# resp = requests.post().text
# print(resp)