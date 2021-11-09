import csv

import requests
from lxml import etree

file =open(r'C:\CodeTime\JsSpider\zhihu\hotrank.csv',mode='a',encoding='utf-8',newline='')
csv_write = csv.DictWriter(file,fieldnames=['标题','文章链接','正文','热度','图片'])
csv_write.writeheader()


def data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        # 'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': '_zap=daeb4fcf-2136-49a8-83bb-faef8377ade7; d_c0="ADBd43cq2ROPTuL2xQ7xQO_2Xr8PFKCy5Ns=|1633771270"; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=i9kzzuP8hjFEERUBAQY7pT1hZqxgmGfZ; _xsrf=vTJ1P23X2BDuiJ1gL71lybCdk4jkNIGg; __snaker__id=Jdg4XtHbPpb2gONN; gdxidpyhxdE=ny367fm7pUqA6oUUxEJgHvOLQtc%2BOu6luZbWDO%5CD%5CwSrtkUovbL170LZmMW3P2ekL%5CYp9%2BRXj9rDuwlvwJuXamcyU4BEQ2nSk%2B8VyxVKZ0TfIM1YRf%2FYLntefJxZb1d8ZZbPMo7A%5Cq76sUXP53YCgdDw%2B4aaVZOWQEoc%5CUjekzsyu1dk%3A1634797081307; YD00517437729195%3AWM_NI=bJCjGvc7jGzECYrOgg4vOmyI%2FzCr9DAGCSZ4f39aDtvD8qjnYCBOFYG5QDNR3vXINZKZPYLUTSmcbXVpzf2NRrLTNi1uNi5mtWRkn7FsAzxICe9C%2BYul2ClT0OH61AnEbUw%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eed9f2409686a3b6c24aacef8fa7d85e838a8abab679a8b588adf66d91bb8d8fc42af0fea7c3b92aa2968d8bc67ea1e9a6a8f94f8187beb0e66df8aa818efc43eda68d93bc5083998db4d940a6edf782c780b69cf892e9669b9d8eb0c55385eb9fa5cd5af1aa98aacd528986a0bacf5f988da384e15496b0b687b14692ae84b5cd63f3ab828ab867b8899e8ced3d86ad8f9bfb4381bbf7a4aa53b7b4fea4ef60f49188d7b44bae9baeb6f637e2a3; captcha_session_v2="2|1:0|10:1634796183|18:captcha_session_v2|88:Vjg4MUk5ZURpQlJQL3d6S0ZhY3hDelVacHRzYWdPMlpjditJOGx3cmI5aVhWZDc5aEZWajh4cUZUT21ZSzR4Sw==|e00a94f6b5d815a77b986490c2df391bf21543055621d974f2381b154d7b5556"; captcha_ticket_v2="2|1:0|10:1634796202|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfbDZXV3NoX3FKT3hxTU5PbEM0OFM0djdfQmNULWNxMS14TXQySGQxeTFUVlZsRGRlbHlXSU9URG5lLnItWm9aZUhfbExLN3I5dzJwMHJ3ZjQyUHVxRGQtc3Y1N2prWC11LW9ia2VlTHFmWjItc0kubW96QkZQVG9kMUZoYV9oRlNGLndRV2JSSmZWeUhCaGluaEs5a2Z4SHBCNmpzSnZUaTR6WEpXMFVzWDhHVC5KY1NXMV96c3VjQk5jd08udG5kdW1Ud3hudTE5QTYtZUdfUjJXa1ZvQ0Z0am02ZWhoQ2Z1OVdFc19MSVR3VVNhVThrVF9DUGRRVDhRZ1NWZXl0Nkl5R0xQRXdhVVhaUWljOEtFRElBX2hyNjRsUEVMVGsxNHFJU1VkYW56NGEtVjRaSzJyQ0oxNV9aZDc2ZENnOGRXbzlJVzRVTGdiZGtoc2RTSTdzZGF1b0FjYWdtaHdJc3ZTbEJPdGNmaWg4NGV6MDlVdkNDVlBlRW9acUZGZHU5RmVQUWRkaVM5MU5FZTJNX19GLlRNYTd4aDFtN2FGZjRKdklkSmRCVTVWQWU0bHMyUXlhWnRWbjhsTWlnNnY4ZC5mbHpqWS5zazdjRURJMm9iQW5MN280WW9hbUJJeDhrWmpqN1pqTXhfa2VFWXRFZVl6eHdHcnJvQ3RtMyJ9|b5db3d3b94475e9936d675b134181e7ff9cfe04a1eaa1a677f9f5d075e17db51"; r_cap_id="NWIwNTQ3MjZjM2Y4NDU0NWI5NzkzNWYxYzI2MGE4ZTE=|1634796205|a83f2f3d6eb3a87d078d17a3dc0d093874ce3899"; cap_id="NTg3ZjRjNzUwYzgyNDFlZDg0MzFiNWFhOWI2ZjJlMTk=|1634796205|cab976b3c706c96b5a457d64685073d912a09ce8"; l_cap_id="MjA1OTBlZjdjNDIwNGMwODkzY2E3YWMwNWZmNDg4N2Q=|1634796205|13248d312362d7381ec334a73303b4ad0900aac0"; capsion_ticket="2|1:0|10:1634796209|14:capsion_ticket|44:OGRlMzU2NzAzZGRjNDdjYjk1MWM3NGMxN2YwZTA2NDY=|14f4fea871cdabe7a1593be952baa2cd551e59b62cc3ad3a8ae41e5c6812ed03"; client_id="NjUxODQxREEwNDkyMEVEMEI4RTNBQzI0Q0VFMzUyQjA=|1634796220|f1942eb7e963236aaf0d1811ec283dab0ad64a2d"; z_c0="2|1:0|10:1634796258|4:z_c0|92:Mi4xZ19Nd013QUFBQUFBTUYzamR5clpFeVlBQUFCZ0FsVk40bEJlWWdENzk4Z1ItSW9CTm0tY3dOVHItd05zUW9XM05R|98d1f6d7d69fd683eb6419c073c11bb11a357d331494a2c4a5ca908d71eef3a3"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1636429547,1636437721,1636442901,1636450758; NOT_UNREGISTER_WAITING=1; SESSIONID=jRcMJ7hR8rB9cCVOEvsliTAU2r5crt6K6nvYn5fJqG5; JOID=V1AWAk2O1Vbly0y_L4obwLu0Ymg66Yw3r4J23H-1qh_erwzka8SZ2YDFSrYqWqqNdxjmE_z6QBm7gqLBmXBofio=; osd=UF4TA0qJ21PkzEuxKoscx7WxY28954k2qIV42X6yrRHbrgvjZcGY3ofLT7ctXaSIdh_hHfn7Rx61h6PGnn5tfy0=; tst=h; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1636451905; KLBRSID=5430ad6ccb1a51f38ac194049bce5dfe|1636452108|1636442900'
    }
    resp = requests.get(url=url,headers=headers).text
    html = etree.HTML(resp)
    return html

def parse(html):
    items = html.xpath('//div[@class="HotList-list"]/section')
    for item in items:
        title = item.xpath('./div[@class="HotItem-content"]/a/h2/text()')[0]
        link = item.xpath('./div[@class="HotItem-content"]/a/@href')[0]

        text = item.xpath('./div[@class="HotItem-content"]/a/p/text()')
        if len(text) >0:
            text = text[0]
        else:
            text = None
        hot = item.xpath('./div[@class="HotItem-content"]/div/text()')[0]
        # hot = hot[0]
        img = item.xpath('./a/img/@src')
        if len(img) >0:
            img = img[0]
        else:
            img = None
        data_dict = {'标题': title, '文章链接': link, '正文': text, '热度': hot, '图片': img}
        save(data_dict)

def save(dict):
    csv_write.writerow(dict)

if __name__ == '__main__':
    url = 'https://www.zhihu.com/hot'
    html = data(url)
    parse(html)

