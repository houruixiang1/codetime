import requests
import json

url = 'https://match.yuanrenxue.com/jssm'
session = requests.Session
headers= {
    'user-agent': 'yuanrenxue.project',
    'referer': 'https://match.yuanrenxue.com/match/3',
    # 'cookie': 'qpfccr=true; no-alert3=true; tk=-5571397726181509472; sessionid=zgm0rlsvh3lgtakbwshm3tolg7ompi53; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1635344413; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1635344391,1635347932; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1635348920; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1635348942'
}
session.headers = headers
resp = session.post(url=url,headers=headers)
print(resp.cookies)