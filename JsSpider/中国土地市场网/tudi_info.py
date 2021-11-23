import csv
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Queue
from JsSpider.proiex.proiex import get_pro
import requests
queue_list = Queue()
# file =open('C:\CodeTime\csv\中国土地市场网供地结果.csv',mode='a',encoding='utf-8',newline='')
# csv_write = csv.DictWriter(file,fieldnames=["gdGuid", "xzqDm","tdZl","gyFs","gyMj","tdYt","qdRq","xzqFullName"])
#
# csv_write.writeheader()
def handel(data):
    url = 'https://api.landchina.com/tGdxm/result/list'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '55',
        'Content-Type': 'application/json',
        'Hash': '8d80bd02ea77e38a4f4de82d5054d50df479c8cadd9a407e5939c4c6b6f9b45f',
        'Host': 'api.landchina.com',
        'Origin': 'https://www.landchina.com',
        'Referer': 'https://www.landchina.com/',
        # sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"
        # sec-ch-ua-mobile: ?0
        # sec-ch-ua-platform: "Windows"
        # Sec-Fetch-Dest: empty
        # Sec-Fetch-Mode: cors
        # Sec-Fetch-Site: same-site
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    data = {
        'endDate': "",
        'pageNum': 1,
        'pageSize': 10,
        'startDate': ""
    }
    # task = get_pro()
    # proxie = {'http': '180.119.83.230:9999'}
    resp = requests.post(url=url,headers=headers,json=data).json()
    return resp
def parse(data,i):
    resp = handel(data)
    # print('hello',resp)
    if 'data' not in str(resp):
        print("第%s页请求失败" % i)
        return 'shibai'
    else:
        dict = {}
        for j in resp['data']['list']:
            gdGuid = j["gdGuid"]
            # print(gdGuid)
            xzqDm = j["xzqDm"]
            tdZl = j["tdZl"]
            gyFs = j["gyFs"]
            gyMj = j["gyMj"]
            tdYt = j["tdYt"]
            qdRq = j["qdRq"]
            xzqFullName = j["xzqFullName"]
            dict = {
                "gdGuid":gdGuid, "xzqDm":xzqDm,"tdZl":tdZl,"gyFs":gyFs,"gyMj":gyMj,"tdYt":tdYt,"qdRq":qdRq,"xzqFullName":xzqFullName
            }
            # file = open('C:\CodeTime\csv\中国土地市场网供地结果.csv', mode='a', encoding='utf-8', newline='')
            # csv_write = csv.DictWriter(file,fieldnames=["gdGuid", "xzqDm","tdZl","gyFs","gyMj","tdYt","qdRq","xzqFullName"])
            # csv_write.writeheader()
            # csv_write.writerow(dict)
            # print("第i页" % i,dict)
        print('第%d页数据存入完毕！！！' % i,dict)
def page_handel():
    for i in range(1,100):
        data = {
            'endDate': "",
            'pageNum': i,
            'pageSize': 10,
            'startDate': ""
        }
        queue_list.put({'data':data,'i':i})
page_handel()
# resp = handel(1)
# print(resp)
pool = ThreadPoolExecutor(max_workers=4)
while queue_list.qsize() > 0:
    pool.submit(parse,queue_list.get('data'),queue_list.get('i'))
    # print(queue_list.get("i"))
    # parse(queue_list.get('data'),queue_list.get('i'))