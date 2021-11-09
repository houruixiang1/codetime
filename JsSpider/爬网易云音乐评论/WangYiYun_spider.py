import json

import requests
from Crypto.Cipher import AES
from base64 import b64encode
data ={
    "cursor": -1,
    "offset": 0,
    "orderType": 1,
    "pageNo": 1,
    "pageSize": 20,
    "rid": "R_SO_4_1490566032",
    "threadId": "R_SO_4_1490566032"
}

# '''
# function a(a) {
#         var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
#         for (d = 0; a > d; d += 1)
#             e = Math.random() * b.length,  #随机数
#             e = Math.floor(e),  # 取整
#             c += b.charAt(e);  # 转换
#         return c
#     }
#     function b(a, b) {  # 第一次a：
#         var c = CryptoJS.enc.Utf8.parse(b)
#           , d = CryptoJS.enc.Utf8.parse("0102030405060708")
#           , e = CryptoJS.enc.Utf8.parse(a)
#           , f = CryptoJS.AES.encrypt(e, c, {
#             iv: d,
#             mode: CryptoJS.mode.CBC
#         });
#         return f.toString()
#     }
#     function c(a, b, c) {
#         var d, e;
#         return setMaxDigits(131),
#         d = new RSAKeyPair(b,"",c),d
#         e = encryptedString(d, a)
#     }
#     function d(d, e, f, g) {
#         var h = {}
#           , i = a(16);  # 16位的随机数
#         return h.encText = b(d, g),
#         h.encText = b(h.encText, i),
#         h.encSecKey = c(i, e, f),
#         h
#     }
#     window.asrsea = d,
# '''
def get_encSecKey():
    return "72b5063e6577f006d19f11768f84e98e6abd73157db3d04e703253250946bc7a9a19fe4d26754e9536573e967a9657ada7b6b9873a511f7943e47ae63b094a00e874769aa7355553304da3f737903ccb60457b2917268d147a587953e88976947e617659485c6b26894c6103efac8ab2578bcf26635ba2e257f1b6c6437ef265"


def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data

def enc_params(data,key): #加密过程
    iv = '0102030405060708'
    data = to_16(data)
    aes=AES.new(key=key.encode('utf-8'),IV=iv.encode('utf-8'),mode=AES.MODE_CBC)
    bs = aes.encrypt(data.encode('utf-8'))
    return str(b64encode(bs),'utf-8')

def params_value(data):   # 字符串
    first = enc_params(data,g)
    second = enc_params(first,i)
    return second

e = '010001'
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
i = 'YrVZZispzSTaWqEA'
g = '0CoJUm6Qyw8W8jud'
# (d,e,f,g)
# (data,'010001',很长，'0CoJUm6Qyw8W8jud')
url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
value={
    "encSecKey":get_encSecKey(),
    "params": params_value(json.dumps(data))
}
resp = requests.post(url=url,headers=headers,data=value).json()
hot_comment = resp['data']['hotComments']
for comment in hot_comment:
    comment_content = comment['content']
    print(comment_content)
