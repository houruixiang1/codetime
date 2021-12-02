import base64
import re

import requests
from fontTools.ttLib import TTFont
url= "https://www.maoyan.com/board/1"
resp = requests.get(url).text
print(resp)
# piaofang = re.search('<span class="stonefont">(.*?)</span>',resp,re.S).group(1).strip()
# print(piaofang)
woff_link = re.search("   url\('(.*?)'\) format\('woff'\);",resp,re.S).group(1).strip()
real_woff_link = 'http:' + woff_link

with open(r'C:\CodeTime\js\maoyan_2.woff', 'wb')as f:
    content = requests.get(url=real_woff_link).content
    # print(content)
    f.write(content)
font = TTFont(r'C:\CodeTime\js\maoyan_2.woff')
font.saveXML(r'C:\CodeTime\js\maoyan_2.xml')
# font = TTFont(r'C:\CodeTime\js\7_1.woff')
# font.saveXML(r'C:\CodeTime\js\7_2.xml')