import requests
import execjs
# pwd = '12345678'
node = execjs.get()

jsinfo = '''
    const CryptoJS = require('crypto-js');
    function jslencode(text, aes_key) {
    var key = CryptoJS.enc.Utf8.parse(aes_key);
    var iv = CryptoJS.enc.Utf8.parse("");
    var srcs = CryptoJS.enc.Utf8.parse(text);
    var encrypted = CryptoJS.AES.encrypt(srcs, key, {
        iv: iv,
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return encrypted.ciphertext.toString(CryptoJS.enc.Hex)
}
'''
ctx = execjs.compile(jsinfo, cwd=r"C:\clip-spider-v2\node_modules")
username = ctx.call('jslencode',18737540525,'397151C04723421F')
password = ctx.call('jslencode','hrx114526','397151C04723421F')
# ctc = node.compile(open(r'C:\CodeTime\JsSpider\login\集思录login.py',mode='r',encoding='utf-8',cwd=r"node_modules").read())
# funcName = 'jslencode("{0}","{1}")'.format(121345678,'397151C04723421F')
# password = ctc.eval(funcName)
# print(username,password)
data= {
'return_url': 'https://www.jisilu.cn/account/find_password/modify/mobile_1__key-fe6b60ab8dcd02a49a75',
'user_name': username,
'password': password,
'net_auto_login': 1,
'_post_type': 'ajax',
'aes': 1
}
resp = requests.post('https://www.jisilu.cn/account/ajax/login_process/',data=data)
print(resp.cookies)
