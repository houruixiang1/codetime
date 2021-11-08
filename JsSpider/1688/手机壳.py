# coding:utf-8

import re

import requests



def get_urls(url):
    """获取查询商品的每家店的地址"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        # 'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate',
        # 'Connection': 'keep-alive'
        }
    html = requests.get(url=url, headers=headers).text
    # print(html)
    return html
def get_jsondata(html):
    json_data = re.search('<script type="text/javascript">(.*?)</script>',html,re.S).group(1).strip()
    # print(json_data)
    real_data = re.search('var pageConfig = \{(.*?)\}(\s+)var p4pObject',json_data,re.S).group(1).strip()
    # print(real_data)
    price_list = []
    title_list = []
    titles = re.finditer('"title":"(.*?)"',real_data,re.S)
    for title in titles:
        title = title.group(1)
        # print(type(title))
        title = title.replace('<font color=red>','').replace('</font>','').strip()
        title_list.append(title)
    prices = re.finditer('"strPriceMoney":"(.*?)"',real_data,re.S)
    for price in prices:
        price = price.group(1)
        price_list.append(price)

    print(title_list)
    print(price_list)

def main():
    url = "https://p4psearch.1688.com/p4p114/p4psearch/offer.htm?keywords=%CA%D6%BB%FA%BF%C7&n=y&netType=1%2C11%2C16&page-source=sem&cosite=baidujj_pz&keywordid=&trackid=885662561117990122602&location=re&spm=a260k.dacugeneral.search.0"
    html = get_urls(url)
    # print(html)
    get_jsondata(html)

if __name__ == "__main__":
    main()
