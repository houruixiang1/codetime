import re
import pandas as pd

import numpy
import requests

url= 'http://xxfb.mwr.cn/hydroSearch/greatRiver'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
}

rexp = requests.get(url=url,headers=headers,verify=False).json()
# print(rexp)
dateTime_list = []
zl_list = []
poiAddv_list = []
poiBsnm_list = []
ql_list = []
rvnm_list = []
stnm_list = []
wrz_list = []
for i in rexp['result']['data']:
    data = i
    # print(data)
    dateTime = re.findall("'dateTime': '(.*?)'", str(data), re.S)[0]
    dateTime_list.append(dateTime)

    poiAddv = re.findall("'poiAddv': '(.*?)'", str(data), re.S)[0]
    poiAddv_list.append(poiAddv)

    poiBsnm = re.findall("'poiBsnm': '(.*?)'", str(data), re.S)[0]
    poiBsnm = str(poiBsnm).strip()
    poiBsnm_list.append(poiBsnm)

    ql = re.findall("'ql': (.*?),", str(data), re.S)[0]
    ql_list.append(ql)

    rvnm = re.findall("'rvnm': '(.*?)'", str(data), re.S)[0]
    rvnm = str(rvnm).strip()
    rvnm_list.append(rvnm)

    # stcd = re.findall("'stcd': '(.*?)'", str(data), re.S)[0]
    # stcd_list.append(stcd)

    stnm = re.findall("'stnm': '(.*?)'", str(data), re.S)[0]
    stnm = str(stnm).strip()
    stnm_list.append(stnm)

    # tm = re.findall("'tm': '(.*?)'", str(data), re.S)[0]
    # tm_list.append(tm)
    #
    # webStlc = re.findall("'webStlc': '(.*?)'", str(data), re.S)[0]
    # webStlc_list.append(webStlc)

    wrz = re.findall("'wrz': (.*?),", str(data), re.S)[0]
    wrz_list.append(wrz)

    zl = re.findall("'zl': (.*?)}", str(data), re.S)[0]
    zl_list.append(zl)

head = ['流域', '行政区', '河名', '站名', '时间', '水位(米)', '流量(米^3/秒)', '警戒水位(米)']  # 表头数据
list = [poiBsnm_list, poiAddv_list, rvnm_list, stnm_list, dateTime_list, zl_list, ql_list, wrz_list]  # 数据列表
list_change = numpy.transpose(list)  # 数据行列互换
test = pd.DataFrame(columns=head, data=list_change)
test.to_csv(rf'C:\CodeTime\csvfile\全国水雨情信息网站.csv')

# print(dateTime_list)

    # for j in i:
    #     dateTime = j[0]
    #     print(dateTime)
