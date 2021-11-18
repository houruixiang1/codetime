import execjs

# jsinfo = '''
#      const Cr = require("crypto-js");
# function encode(t) {
#     var e = Cr.enc.Utf8.parse("G3JH98Y8MY9GWKWG")
#       , a = Cr.enc.Utf8.parse(t)
#       , A = Cr.AES.encrypt(a, e, {
#         mode: Cr.mode.ECB,
#         padding: Cr.pad.Pkcs7
#     });
#     return encodeURIComponent(A.toString())
# }
# function d(t) {
#     var xx = encode(t)
#     return encodeURIComponent(xx)
# }
# '''
with open(r"C:\CodeTime\JsSpider\login\js\财新password.js",mode='r',encoding='utf-8')as f:
    jsinfo = f.read()

ctx = execjs.compile(jsinfo, cwd=r"C:\clip-spider-v2\node_modules")
password = ctx.call('d',123456)
print(password)