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
    name = html.xpath('//ul[@class="book-chapter-list"]/li[2]/a/text()')
    link = html.xpath('//ul[@class="book-chapter-list"]/li[2]/a/@href')
    name = name[0].strip()
    vid = link[0].split('/')[-1]
    # print(vid)
    return name,link,vid

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
    # cook = str(resp1.cookies)
    # ci_session = re.search(' (.*?) ',cook,re.S).group(1).strip()
    # print(ci_session)
    # key = ci_session.split('=')[0]
    # value = ci_session.split('=')[1]
    # print(key,value)
    # session.cookies.set(key,value)
    # print(session.cookies)
    chapter_access_key = response['chapter_access_key']
    # print(chapter_access_key)
    url = 'https://www.ciweimao.com/chapter/get_book_chapter_detail_info'
    headers = {
        'Host': 'www.ciweimao.com',
        'Origin': 'https://www.ciweimao.com',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
        'Referer': 'https://www.ciweimao.com/chapter/{}'.format(vid),
        'X-Requested-With': 'XMLHttpRequest'
    }
    data = {
        'chapter_id': vid,
        'chapter_access_key': chapter_access_key
    }
    resp = session.post(url=url,headers = headers,data=data).json()
    # print(resp)
    chapter_content = resp['chapter_content']
    encryt_keys = resp['encryt_keys']
    # print(encryt_keys)
    return chapter_access_key,chapter_content,encryt_keys

def main():
    node = execjs.get()
    with open(r"C:\CodeTime\js\test.js",encoding='utf-8') as f:
        info = f.read()
    # print('123454566',info)
    # js = '''
    #    const CryptoJS = require('crypto-js');
    # '''
    # js = js + info
    # print(js)
    # ctc = node.compile(info,cwd=r'C:\CodeTime\node_modules')
    ctc = node.compile(info)
    funcName = 'get_data()'
    # funcName = 'get_data("{0}","{1}","{2}")'.format(accesskey,content,key)
    data = ctc.eval(funcName)
    return data

if __name__ == '__main__':
    start_url = 'https://www.ciweimao.com/book/100276252'
    name = get_vid(start_url)[0]
    # link = get_vid(start_url)[1]
    vid = get_vid(start_url)[2]
    # print(name,vid)
    get_content_and_key(vid)
    accesskey = get_content_and_key(vid)[0]
    content = get_content_and_key(vid)[1]
    key = get_content_and_key(vid)[2]
    # print(accesskey,content,key)
    real_data = main()
    print(real_data)