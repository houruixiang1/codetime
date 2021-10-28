import requests
from requests import sessions


def get_cookie(page):
    url = 'https://match.yuanrenxue.com/jssm'

    headers = {
        'Host': 'match.yuanrenxue.com',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.10 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Accept': '*/*',
        'Origin': 'https://match.yuanrenxue.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://match.yuanrenxue.com/match/3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    session = requests.Session()
    session.headers = headers
    cookies = {'Cookie':'sessionid=6hbehfd0w4y3f0g3h43lyzp6qcedyuyj;'}
    session.post(url,cookies = cookies)
    if page == 4 or page == 5:
        headers['user-agent'] = 'yuanrenxue.project'
    api_url = 'https://match.yuanrenxue.com/api/match/3?page={}'.format(page)
    resp = session.get(url=api_url).json()
    for j in resp['data']:
        value_list.append(j['value'])
if __name__ == '__main__':
    value_list = []
    for i in range(1,6):
        get_cookie(i)
    # print(value_list)
    max_value = max(value_list, key=value_list.count)
    print(max_value)