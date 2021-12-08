import requests
sess = requests.session()
headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1638949382; qpfccr=true; no-alert3=true; tk=2324858437251957931; sessionid=rhkmx30l21r21xouvo9f2ph43qqkuf0o; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1638949406; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1638949406; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1638949417',
    'referer': 'https://match.yuanrenxue.com/match/19',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}
url = 'https://match.yuanrenxue.com/api/loginInfo'
resp = sess.get(url=url,headers=headers)
print(resp.headers)
url1 = 'https://match.yuanrenxue.com/api/match/17'
response = sess.get(url=url1,headers=headers)
print(response.text)
