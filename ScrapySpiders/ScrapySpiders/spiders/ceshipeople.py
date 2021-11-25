# -*- coding: utf-8 -*-
import json
import logging
import os
import re
import time
from selenium import webdriver
from distutils.util import strtobool

from ..database_tool import DBConnector
from ..items import CeshiItem
import redis
import requests
import scrapy
from scrapy.utils.project import get_project_settings
from scrapy_redis.spiders import RedisSpider
from urllib.request import urlretrieve
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


class CeshipeopleSpider(RedisSpider):
    name = "ceshipeople"
    allowed_domains = ['people.com','search.people.cn']
    # start_urls = ['people.com','search.people.cn']
    # handle_httpstatus_list = [418]  # http status code for not ignoring
    redis_key = 'ceshipeople:start_urls'

    def __init__(self, keyword, node='master', uu_id='000000002021', operation="or", crawl_image='True', crawl_video='False', important_user='False', schedule='False', *args, **kwargs):
        super(CeshipeopleSpider, self).__init__(*args, **kwargs)
        self.__task_id = uu_id
        self.keywords = list(filter(None, keyword.split('|')))
        self.operation = operation
        self.redis_key = self.redis_key+"_"+uu_id
        self.crawl_image = strtobool(crawl_image)
        self.crawl_video = strtobool(crawl_video)
        self.important_user = strtobool(important_user)
        self.node = node
        self.js = [0,3,5]
        self.schedule = strtobool(schedule)
        if self.important_user:
            self.uid_list = self.get_important_user()

        if not os.path.exists('/data/'):
            os.makedirs('/data/')

        if node == 'master':
            settings = get_project_settings()
            r = redis.Redis(host=settings.get("REDIS_HOST"), port=settings.get("REDIS_PORT"), decode_responses=True)
            url ='http://search.people.cn/search-platform/front/search'
            # print("hello99",self.parse_page_num())
            pages = self.parse_page_num()
            # print(pages)
            # for page in pages:
            for i,j in enumerate(self.js):
                page = pages[i]
                # print(page)
                page_num = min(page,10)
                for x in range(1, page_num):
                    request_data = {
                        'url': url,
                        'meta': {'key_words': self.keywords,
                                 'page':x,
                                 'type':j
                                 }
                    }
                    r.lpush(self.redis_key, json.dumps(request_data))  #1.r.lpush列表  2.字典转换为字符串
                    # print(r.lrange(self.redis_key,0,1))

    def make_request_from_data(self, data):
        data = json.loads(data)  #字符串转换为字典
        # print(data)
        url = data.get('url')
        meta = data.get('meta')
        for kw in self.keywords:
            # logging.log(msg="Fetch url:"+url, level=logging.INFO)
            return scrapy.Request(url=url, method="POST",headers={
                                    "content-type": "application/json; charset=UTF-8",
                                    "cookie": "Cookie: __jsluid_h=b8062478ebf28d0e7fc3028db63168cb; sso_c=0; sfr=1; wdcid=1ad2449c65c9061e",
                                    "Referer": "http://search.people.cn/s/?",
                                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
                                },body=json.dumps({
                                    'endTime': 0,
                                    'hasContent': 'true',
                                    'hasTitle': 'true',
                                    'isFuzzy': 'true',
                                    'key': kw,
                                    'limit': 10,
                                    'page': meta["page"],
                                    'sortType': 2,
                                    'startTime': 0,
                                    'type': meta["type"],
                                }),callback=self.parse, meta=meta, dont_filter=True)

    def parse_page_num(self):
        page_list = []
        for j in self.js:
            for kw in self.keywords:
                try:
                    content = requests.post(url='http://search.people.cn/search-platform/front/search',
                                headers={
                                    "content-type": "application/json; charset=UTF-8",
                                    "cookie": "Cookie: __jsluid_h=b8062478ebf28d0e7fc3028db63168cb; sso_c=0; sfr=1; wdcid=1ad2449c65c9061e",
                                    "Referer": "http://search.people.cn/s/?",
                                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
                                },
                                json={
                                    'endTime': 0,
                                    'hasContent': 'true',
                                    'hasTitle': 'true',
                                    'isFuzzy': 'true',
                                    'key': kw,
                                    'limit': 10,
                                    'page': 1,
                                    'sortType': 2,
                                    'startTime': 0,
                                    'type': j,
                                }).text
                    # print(content)
                    content_dict = json.loads(content)
                    # print(content_dict)
                    post_count = content_dict['data']['total']
                    page_list.append(post_count)
                except:
                    return "出错！！"
                # print("hello",content_dict)
        return page_list

    def parse(self,response):
        value=response.meta['type']
        data = json.loads(response.text)['data']
        # print("hello1")
        records = data['records']
        # print(data['pages'])
        for record in records:
            if record['belongsName'] != None or " ":
                detail_url = record['url']
                # print("hello",detail_url)
                yield scrapy.Request(url=detail_url, callback=self.parse_text,
                                 meta={'post_item': record,
                                       'type':value}, dont_filter=True)
        # 解析页面，获得目标数据并存储

    def parse_text(self, response):
        user_post_item = response.meta['post_item']
        type = response.meta['type']
        # print("hello2",type)
        # 抓取图片
        if self.crawl_image:
            for i in range(user_post_item['hasImg']):
                pic_url = user_post_item['imageUrl']
                file_name = self.__task_id + '_' + str(user_post_item['id']) + '_' + '1' + '.jpg'
                urlretrieve(pic_url, '/data/' + file_name)
                user_post_item['pics'] = '/data/' + file_name
        else:
            user_post_item['pics'] = None
        # 爬取视频
        if self.crawl_video:
            if type == 5:
                start_url = user_post_item['url']
                # "http://v.people.cn/n1/2021/0203/c431305-32021764.html"
                print(start_url)
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
                }
                resp = requests.get(url=start_url, headers=headers)
                resp.encoding = 'GB2312'
                # print(resp.text)
                opt = re.compile('\{id:"(.*?)",')
                path = opt.search(resp.text, re.S).group(1).strip()
                # print(path)
                start_api_url = 'http://tvplayer.people.com.cn/getXML.php'
                callback = 'playForMobile'
                ios = 0
                api_url = "{}?path={}&callback={}&ios={}".format(start_api_url, path, callback, ios)
                # print(api_url)
                data = {
                    'path': path,
                    'callback': callback,
                    'ios': ios
                }
                response = requests.get(url=api_url, headers=headers,data=data)
                # print(response.text)
                mp4_url = re.search("playForMobile\('(?P<mp4_url>.*?)',", response.text, re.S).group(1).strip()
                # print(mp4_url)
                video_url = mp4_url
                file_name = self.__task_id + '_' + str(user_post_item['id']) + '.mp4'
                try:
                    res = requests.get(video_url, stream=True)
                    with open('/data/' + file_name, "wb") as mp4:
                        for chunk in res.iter_content(
                                chunk_size=1024 * 1024):
                            if chunk:
                                mp4.write(chunk)
                    if os.path.getsize('/data/' + file_name) > 500 * 1024:
                        user_post_item['video'] = '/data/' + file_name
                    else:
                        user_post_item['video'] = None
                except:
                    logging.log(msg=time.strftime("%Y-%m-%d %H:%M:%S [KeyWordsSpider] ")
                                    + "KeyWordsSpider" + ": failed to download video:"
                                    + file_name, level=logging.INFO)
                    user_post_item['video'] = None
            else:
                user_post_item['video'] = None
        else:
            user_post_item['video'] = None

        item = self.parse_field(user_post_item)

        yield item

    def parse_field(self, item):
        user_post_item = CeshiItem()
        user_post_item['uu_id'] = self.__task_id
        user_post_item['title'] = item['title']
        user_post_item['id'] = item['id']
        user_post_item['source'] = item['source']
        user_post_item['text'] = item['content']
        user_post_item['created_at'] = item['displayTime']
        user_post_item['text_url'] = item['url']
        user_post_item['belongsName'] = item['belongsName']
        user_post_item['editor'] = item['editor']
        user_post_item['hasImg'] = item['hasImg']
        if item['hasImg'] > 0:
            user_post_item['pics'] = item['pics']
        else:
            user_post_item['pics'] = None
        user_post_item['video'] = item['video']
        return user_post_item

    def get_important_user(self):
        db_connector = DBConnector()
        db, client = db_connector.create_mongo_connection()
        uid_list = db['uidList'].find()
        uid_list = list(uid_list[0].keys())[1:]
        return uid_list

