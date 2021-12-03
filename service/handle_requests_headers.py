import re

import pandas as pd

with open(r'C:\CodeTime\service\请求头文件.txt',mode='r',encoding='utf-8')as f:
    strs = f.readlines()
# print(len(strs))
for i,str in enumerate(strs):
    s = re.findall('(.*?): (.*)', str.strip(), re.S)
    if '537.36' in s[0][1]:
        ss = "'" + s[0][0] + "'" + ": " + "'" + s[0][1] + "'"
    else:
        ss = "'" + s[0][0] + "'" + ": " + "'" + s[0][1] + "'" + ","
    with open(r'C:\CodeTime\service\处理后请求头文件.txt', mode='a', encoding='utf-8')as f:
        f.write(ss + '\n')


