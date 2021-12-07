

import requests
import re

from lxml import etree

url = "http://glidedsky.com/level/web/crawler-basic-1"
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'footprints=eyJpdiI6InhrdGF3ckV0QlgxMXZiTHNVOTJqQVE9PSIsInZhbHVlIjoiZkNlZHlaNGZRbVwvZGpUU3JxXC9NVVRuRFRVRHJVYmVKSDVNVXhUVWZVNEpsdmg5bUVsWGZVbllyZjdMeThZQk9EIiwibWFjIjoiOTYxN2IxNzdiM2JkNTY2NDE3NGE2MTEwOGU4Mzc2YTc2MzIxZWZjODEwN2Q2NmVlMDRjYzk4OGUxNTRmN2Y3MCJ9; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1638870573; _ga=GA1.2.67459588.1638870573; _gid=GA1.2.1994532581.1638870573; __gads=ID=25e7fc3f519656cf-22b776e95ecf00bc:T=1638870572:RT=1638870572:S=ALNI_MbK_SlwyFFFh1eSe2erRRx-crXY8g; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IllHVEVUU1YyRExlMXpnOFBkSEtta3c9PSIsInZhbHVlIjoiUThaN0JxOEhyR0s3MkIyT0FYZDJPeG9YcGNjMktONjZjQWhkUXNUenhBSm14R1ZyNkpiMGs2czFnbElrbW1aV3IzdWsxbVpjTzJ2eFdzMzJGVmFuK1lHOWkzb29YWGc0WFpoejNNU2ZTOGU0NnJMSENwNHlIc3lGRitsM1JySTZ3YWNMMmpUSGt3d3U5T0wyS2RoeWg5emFvTGtCQnhGSlQ1T0tWTjZKV3BJPSIsIm1hYyI6IjM3NWY1NDA5YWJjMDNiNDFlZDM5YTZhZDhmNDY1MjVmNDFkZTBkZTQ4YWI3MjliZTZkMTNiMDlkMDQ1N2YyMzYifQ%3D%3D; XSRF-TOKEN=eyJpdiI6InJxbDcxQVNYaUFkWGoxS1Z4Tnhsbnc9PSIsInZhbHVlIjoiaklCbytQWDZaa3dLaXJYaU9cLzVQaDdCaUJDQXQxeWd2cG5jQk5rNHRpTTJodXRtM3pnOXA1Q09WRmlaSlpkY3ciLCJtYWMiOiIxNzUwYTRlZmNmMmY4YTY4MDVlM2I3MDdkN2ZjYjM2MTE1OTk0NWE3YjA4YzRkZjZkN2EyM2I1YmUzOWJiMmU2In0%3D; glidedsky_session=eyJpdiI6InlXeVhBcklPMExDc0FBZmNxUWNwa0E9PSIsInZhbHVlIjoibWVxR1NIRmE3RlgyNUsxb1g0ZU5iYmU4aUFqelVTWlwvXC9GZkRubkQwd1IxcUVZZW5uNWoyeHZBRFM2QlZzb2NZIiwibWFjIjoiYjZiYTg4ZjdkMzY1ODU4NTY0ZjVhM2M3YTc4ZTRlNTU1MTBmN2U4ZWY1Y2RjMjMyYjE1NGI0YWJhMWEzZjQ2YyJ9; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1638871030',
    'Host': 'glidedsky.com',
    'Referer': 'http://glidedsky.com/level/crawler-basic-1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
resp = requests.get(url=url,headers=headers).text
# print(resp)
html = etree.HTML(resp)
# rr = re.findall('<div class="col-md-1"> (.*?) </div>',resp,re.S)
# print(rr)
# for r in rr:
#     print(r)
value_list = []
lists = html.xpath('//div[@class="row"]/div')
for list in lists:
    value = list.xpath('./text()')
    value_list.append(int(value[0].strip()))

print(value_list)
total = sum(value_list)
print(total)