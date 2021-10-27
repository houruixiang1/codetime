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
            'cookie': 'sessionid=jbzwkkh8ma1dowq2jb6e2wmd85a8amow;'
        }
        resp = requests.get(url=start_url,headers=headers).json()
        for j in resp['data']:
            list.append(j['value'])
    # print(list)
    sum = sum(list)
    print(sum)
