import requests
import json
import base64

def base64encrypt(content):
    return base64.b64encode(content.encode('utf-8')).decode('utf-8')


if __name__ == '__main__':
    list = []
    for i in range(1,6):
        # url = urls.format(i,lists[-1+i])
        # print(url)
        content ='yuanrenxue' + str(i)
        m = base64encrypt(content)
        # print(i,m)

        start_url = 'https://match.yuanrenxue.com/api/match/12?page={}&m={}'.format(i,m)
        headers = {
            'user-agent': 'yuanrenxue.project',
            'referer': 'https://match.yuanrenxue.com/match/12',
            'cookie': 'vaptchaNetway=cn; Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1635232738; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1635230397,1635299408; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1635232542,1635299408; no-alert3=true; tk=-5571397726181509472; sessionid=jbzwkkh8ma1dowq2jb6e2wmd85a8amow; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1635318997; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1635318999'
        }
        resp = requests.get(url=start_url,headers=headers).json()
        for j in resp['data']:
            list.append(j['value'])
    print(list)
    sum = sum(list)
    print(sum)
