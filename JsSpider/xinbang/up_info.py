# 特别注意requests请求时，带入的参数用（json=data）,否则无法请求成功
import requests
import re

url = 'https://gw.newrank.cn/api/xd/xdnphb/nr/cloud/douyin/searchAccountList'
# keyword = input('请输入一个抖音号的名字：')
headers = {
    # 'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Connection': 'keep-alive',
    # 'content-type': 'application/json',
    'cookie': 'UM_distinctid=17ce8b6c7dd27f-0fc33a5c397409-57b193e-1fa400-17ce8b6c7de9a8; Hm_lvt_a19fd7224d30e3c8a6558dcb38c4beed=1635991865,1636004381; ISFIRSTLOGIN=true; token=79305CDE9BFB4FFCAA2F6EF1C113B440; Hm_lpvt_a19fd7224d30e3c8a6558dcb38c4beed=1636008418',
    # 'Host': 'gw.newrank.cn',
    'n-token': '9116298d52d64bbfb2bafa92267f74f2',
    # 'Origin': 'https://xd.newrank.cn',
    # 'Referer': 'https://xd.newrank.cn/home/search',
    # 'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': "Windows",
    # 'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}
data = {
    "keyword": '人民日报'
}
resp = requests.post(url=url,headers=headers,json=data).json()
print(resp)
# session = requests.session()
# start_url = 'https://gw.newrank.cn/api/xd/xdnphb/nr/cloud/douyin/DOU/search/getSuggestAccountDTO'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
# }
# data = {
#     "key":"account",
#     "keyword":"人民日报"
# }
# resp = session.post(url=start_url,headers=headers)
# print(resp.text)