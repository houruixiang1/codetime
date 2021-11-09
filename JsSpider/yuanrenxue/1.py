import requests
import execjs
import time



# session = requests.session()
# start_url = 'https://match.yuanrenxue.com/api/loginInfo'
# headers = {
#     'cookie': 'vaptchaNetway=cn; Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1635232738; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1636103487,1636105082,1636361584,1636439068; qpfccr=true; no-alert3=true; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1635989789,1636103490,1636361587,1636439071; tk=6392365292107279876; sessionid=ey5ixlzlxkpllna0ti4787kkg8fluh7h; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1636439085; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1636442923',
# }
# resp = session.get(start_url)
# print(resp.text)
node= execjs.get()
ctc = node.compile(open(r'C:\CodeTime\js\1.js',mode='r',encoding='utf-8').read())
funcName = 'get_m()'.format()
m = ctc.eval(funcName)
# print(m)
# m = m + '%E4%B8%A8' + str(int(timestamp/1000))
# print(m)

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'yuanrenxue.project',
    'Host': 'match.yuanrenxue.com',
    'cookie': 'sessionid=ey5ixlzlxkpllna0ti4787kkg8fluh7h;',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://match.yuanrenxue.com/match/1',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
list = []
for i in range(1,6):
    url = 'https://match.yuanrenxue.com/api/match/1?page={}&m={}'.format(i,m)
    resp = requests.get(url=url,headers=headers).json()
    # print(resp.text)
    for j in resp['data']:
        list.append(j['value'])
print(list)
total = sum(list)
print(int(total/50))