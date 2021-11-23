import requests
import json
import warnings
warnings.simplefilter("ignore")


url= 'https://entree-ali.igetget.com/bauhinia/v2/class/lastupdate'
headers = {
    # 'Xi-App-Key': 'android-9.6.0',
    # 'Xi-Uid': '325247571',
    # 'Xi-Thumb': 'xl',
    # 'Xi-Dt': 'phone',
    # 'Xi-Ov': '7.1.2',
    # 'Xi-Net': 'wifi',
    # 'Xi-Os': 'ANDROID',
    # 'Xi-D': '02fa0c2cab821af0',
    # 'Xi-Dv': 'SM-G977N',
    # 'Xi-T': 'json',
    # 'Xi-Chil': '0',
    # 'Xi-V': '2',
    # 'Xi-Av': '9.6.0',
    # 'Xi-Scr': '2.0',
    # 'Xi-Adv': '1',
    # 'Xi-Seid': '02fa0c2cab821af0',
    # 'Xi-Span-Id': '0',
    # 'Xi-Trace-Id': '5c6b3d150493be0c',
    # 'Xi-Parent-Id': '2cf820a4d74179c5',
    # 'Po-Idfa': '0',
    # 'Po-Oaid': '0',
    # 'Po-Android-Id': '02fa0c2cab821af0',
    # 'Po-Ov': '7.1.2',
    # 'Po-Dv': 'SM-G977N',
    # 'G-Auth-Sign': '29c77e493994fa5652ab12ef80589f0ccf8b08bf',
    # 'G-Auth-Nonce': '07badc71478b86894cb4ac6b2a2c03a0',
    # 'G-Auth-Ts': '1637635898',
    # 'G-Auth-Appid': '463ceba202a9f6f9ac4cd98d0f2f2876204ea85c',
    # 'G-Auth-Token': 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJpZ2V0Z2V0LmNvbSIsImV4cCI6MTY0MDIyNzg1MCwiaWF0IjoxNjM3NjM1ODUwLCJpc3MiOiJEREdXIEpXVCBNSURETEVXQVJFIiwibmJmIjoxNjM3NjM1ODUwLCJzdWIiOiIzMjUyNDc1NzEiLCJkZXZpY2VfaWQiOiIiLCJkZXZpY2VfdHlwZSI6IiJ9.RCw6GVuInrPt4lZR78z9oFBSvJAhPuqp5p7MJAgh8faACvMRUkl68UBIe-79yZPIlCWX_MsgG8qd02TJk8LWIQ',
    # 'Host': 'entree-ali.igetget.com',
    'Content-Type': 'application/json; charset=UTF-8',
    # 'Content-Length': '282',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.12.1'
}
data = {
    "rank_type":66002177,
    "h":{
        "u":"325247571","thumb":"xl","dt":"phone","ov":"7.1.2","net":"wifi","os":"ANDROID","d":"02fa0c2cab821af0","dv":"SM-G977N","t":"json","chil":"0","v":"2","av":"9.6.0","scr":"2.0","adv":"1","ts":"1637635898","s":"8b2d550fe07e9409","seid":"02fa0c2cab821af0"
    }
}

resp = requests.post(url=url,headers=headers,json=data,verify=False)

print(resp)