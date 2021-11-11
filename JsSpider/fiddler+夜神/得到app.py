import requests
import json


url= 'https://entree-ali.igetget.com/bauhinia/v2/class/lastupdate'
headers = {
    # 'Host': 'entree-ali.igetget.com',
    # 'Content-Type': 'application/x-www-form-urlencoded',
    # 'Connection': 'Keep-Alive',
    # 'Accept-Encoding': 'gzip',
    # 'User-Agent': 'okhttp/3.12.1'

'G-Auth-Sign': '169cef4b071c96c90cd1bc6b86c3a9dd92025612',
'G-Auth-Nonce': 'fedf2aa8b74ac74616a748c684ae9d36',
# 'G-Auth-Ts': '1636602417',
'G-Auth-Appid': '463ceba202a9f6f9ac4cd98d0f2f2876204ea85c',
'G-Auth-Token': 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJpZ2V0Z2V0LmNvbSIsImV4cCI6MTYzOTE5MzQxNywiaWF0IjoxNjM2NjAxNDE3LCJpc3MiOiJEREdXIEpXVCBNSURETEVXQVJFIiwibmJmIjoxNjM2NjAxNDE3LCJzdWIiOiIzMjUyNDc1NzEiLCJkZXZpY2VfaWQiOiIiLCJkZXZpY2VfdHlwZSI6IiJ9.I-3oNCixwKdKCRN97rJstkeSOIcnVPnvxySBHHZ0BAWwvWOwJN9SsgBgjdUA73DechVZYahEOkxhc8f9ifBOuw',
'Host': 'entree-ali.igetget.com',
'Content-Type': 'application/x-www-form-urlencoded',
'Connection': 'Keep-Alive',
'Accept-Encoding': 'gzip',
'User-Agent': 'okhttp/3.12.1',

}
data = {
    'count': 20,
    'check_buy': 'false',
    'sort': 'newest',
    'h': {
        "u":"325247571","thumb":"xl","dt":"phone","ov":"7.1.2","net":"wifi","os":"ANDROID","d":"02fa0c2cab821af0","dv":"SM-G977N","t":"json","chil":"0","v":"2","av":"9.6.0","scr":"2.0","adv":"1","ts":"1636601477","s":"8b2d550fe07e9409","seid":"02fa0c2cab821af0"
    },
    'page': 0,
    'college_id': 0
}
resp = requests.post(url=url,headers=headers,json=data,verify=False)

print(resp)