import re

import requests

if __name__ == '__main__':
    cookie = {
        'cookie': 'sessionid=jbzwkkh8ma1dowq2jb6e2wmd85a8amow;'
    }
    headers = {
         'user-agent': 'yuanrenxue.project',
    }
    session = requests.Session()
    url = 'https://match.yuanrenxue.com/match/13'
    resp = session.get(url,headers = cookie).text
    # print(resp)
    cookies = re.findall("'([a-zA-Z0-9=|_])'",resp)
    # print(cookies)
    cookies = ''.join(cookies)
    # print(cookies)
    key, value = cookies.split('=')
    session.cookies.set(key, value)
    # print(session.cookies)
    list = []
    for i in range(1, 6):
        api_url = 'https://match.yuanrenxue.com/api/match/13?page={}'.format(i)
        response = session.get(api_url,headers = headers).json()
        for j in response['data']:
            list.append(j['value'])
    sum = sum(list)
    print(sum)
