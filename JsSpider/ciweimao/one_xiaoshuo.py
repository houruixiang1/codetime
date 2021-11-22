import requests
import execjs
import re
from lxml import etree

def get_vid(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    }
    resp = requests.get(url=url,headers=headers).text
    html = etree.HTML(resp)
    # print(html)
    name = html.xpath('//ul[@class="book-chapter-list"]/li[1]/a/text()')
    link = html.xpath('//ul[@class="book-chapter-list"]/li[1]/a/@href')
    name = name[0].strip()
    vid = link[0].split('/')[-1]
    # print(name)
    return (name,link,vid)

def get_content_and_key(vid):
    session = requests.session()
    url1 = 'https://www.ciweimao.com/chapter/ajax_get_session_code'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    }
    data1 = {
        'chapter_id': vid
    }
    # session.headers = header
    resp1 = session.post(url =url1,data=data1,headers=header)
    response = resp1.json()
    chapter_access_key = response['chapter_access_key']
    # print(chapter_access_key)
    url = 'https://www.ciweimao.com/chapter/get_book_chapter_detail_info'
    headers = {
        'Host': 'www.ciweimao.com',
        # 'Origin': 'https://www.ciweimao.com',
        # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
        'Referer': 'https://www.ciweimao.com/chapter/{}'.format(vid),
        # 'X-Requested-With': 'XMLHttpRequest'
    }
    data = {
        'chapter_id': vid,
        'chapter_access_key': chapter_access_key
    }
    resp = session.post(url=url,headers = headers,data=data).json()
    # print(resp)
    chapter_content = resp['chapter_content']
    encryt_keys = resp['encryt_keys']
    return (chapter_access_key,chapter_content,encryt_keys)

def main(accesskey,content,key):
    with open(r'C:\CodeTime\js\ceweimao.js',mode='r',encoding='utf-8')as f:
        js = f.read()
    ctc = execjs.compile(js,cwd=r'C:\clip-spider-v2\node_modules')
    # funcName = 'get_data()'
    funcName = 'get_data("{0}","{1}","{2}")'.format(accesskey,content,key)
    data = ctc.eval(funcName)
    return data

if __name__ == '__main__':
    start_url = 'https://www.ciweimao.com/book/100282110'
    rep = get_vid(start_url)
    name = rep[0]
    link = rep[1]
    vid = rep[2]
    # print(name,link,vid)
    value = get_content_and_key(vid)
    accesskey = value[0]
    content = value[1]
    key = value[2]
    # print(accesskey,content,key)
    real_data = main(accesskey,content,key)
    real_data = str(real_data).replace("<p class='chapter'>　　","").replace("<span>3lQmQS</span></p>",'').strip()
    print(real_data)