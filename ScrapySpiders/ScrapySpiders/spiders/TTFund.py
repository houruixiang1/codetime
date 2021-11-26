import csv
import json
import logging
import os
import re
from ast import literal_eval
from distutils.util import strtobool

import pymysql
import redis
import requests
import scrapy
from scrapy.utils.project import get_project_settings
from scrapy_redis.spiders import RedisSpider

from ..database_tool import DBConnector
from ..items import TTFundItem


class TtfundSpider(RedisSpider):
    name = 'TTFund'
    allowed_domains = ['fund.eastmoney.com']
    # start_urls = ['http://fund.eastmoney.com/']
    redis_key = 'TTFund:start_urls'


    def __init__(self,  node='master', uu_id='000000002021', operation="or", schedule='False', *args, **kwargs):
        super(TtfundSpider, self).__init__(*args, **kwargs)
        self.__task_id = uu_id
        # self.keywords = list(filter(None, keyword.split('|')))
        self.operation = operation
        self.redis_key = self.redis_key + "_" + uu_id
        self.node = node
        self.schedule = strtobool(schedule)

        if not os.path.exists('/data/'):
            os.makedirs('/data/')

        if node == 'master':
            settings = get_project_settings()
            r = redis.Redis(host=settings.get("REDIS_HOST"), port=settings.get("REDIS_PORT"), decode_responses=True)
            page = int(self.page_num())
            for i in range(1,page+1):
                url = 'http://fund.eastmoney.com/data/rankhandler.aspx?op=dy&dt=kf&ft=all&rs=&gs=0&sc=qjzf&st=desc&sd=2020-11-22&ed=2021-11-22&es=0&qdii=&pi={}&pn=50&dx=0'.format(i)
                request_data = {
                    'url': url,
                }
                r.lpush(self.redis_key,json.dumps(request_data))  # 1.r.lpush列表  2.字典转换为字符串
            # print(r.lrange(self.redis_key,0,1))

    def make_request_from_data(self, data):
        data = json.loads(data)  #字符串转换为字典
        url = data.get('url')
        logging.log(msg="Fetch url:"+url, level=logging.INFO)
        return scrapy.Request(url=url, method="GET",headers = {
                                'Accept': '*/*',
                                'Accept-Encoding': 'gzip, deflate',
                                'Accept-Language': 'zh-CN,zh;q=0.9',
                                'Connection': 'keep-alive',
                                # 'Cookie': '_adsame_fullscreen_18186=1; qgqp_b_id=ee1233e00fa4e07a7dded8f556d770c6; st_si=45530255328031; st_asi=delete; ASP.NET_SessionId=txxqh5uhg1ssedu3lv3cqwpf; st_pvi=81886945189301; st_sp=2021-11-22%2016%3A05%3A49; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=7; st_psi=20211122161943682-112200312936-0388307388',
                                'Host': 'fund.eastmoney.com',
                                'Referer': 'http://fund.eastmoney.com/data/diyfundranking.html',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
                              },
                          callback=self.parse,  dont_filter=True)

    def page_num(self):
        url = 'http://fund.eastmoney.com/data/rankhandler.aspx?op=dy&dt=kf&ft=all&rs=&gs=0&sc=qjzf&st=desc&sd=2020-11-22&ed=2021-11-22&es=0&qdii=&pi=1&pn=50&dx=0'
        resp = requests.get(url=url, headers={
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': '_adsame_fullscreen_18186=1; qgqp_b_id=ee1233e00fa4e07a7dded8f556d770c6; st_si=45530255328031; st_asi=delete; ASP.NET_SessionId=txxqh5uhg1ssedu3lv3cqwpf; st_pvi=81886945189301; st_sp=2021-11-22%2016%3A05%3A49; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=7; st_psi=20211122161943682-112200312936-0388307388',
            'Host': 'fund.eastmoney.com',
            'Referer': 'http://fund.eastmoney.com/data/diyfundranking.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
        }).text
        page_num = re.search('allPages:(.*?),',resp,re.S).group(1).strip()
        return page_num

    def parse(self, response):

        resp = response.text
        data = re.search('var rankData = .*?(\[.*?\])',resp,re.S).group(1).strip()
        lists = literal_eval(data)
        for list in lists:
            # print(list)
            item = TTFundItem()
            item['uu_id'] = self.__task_id
            if list.split(',')[0]:
                item['code'] = list.split(',')[0]
            else:
                item['code'] = None
            if list.split(',')[1]:
                item['name'] = list.split(',')[1]
            else:
                item['name'] = None
            if list.split(',')[3]:
                item['zhangfu'] = list.split(',')[3]
            else:
                item['zhangfu'] = None
            if list.split(',')[4]:
                item['fenhong'] = list.split(',')[4]
            else:
                item['fenhong'] = None

            if list.split(',')[5]:
                item['fenhong_num'] = list.split(',')[5]
            else:
                item['fenhong_num'] = None
            if list.split(',')[6]:
                item['start_date'] = list.split(',')[6]
            else:
                item['start_date'] = None
            if list.split(',')[7]:
                item['danweijingzhi1'] = list.split(',')[7]
            else:
                item['danweijingzhi1'] = None
            if list.split(',')[8]:
                item['leijijingzhi1'] = list.split(',')[8]
            else:
                item['leijijingzhi1'] = None
            if list.split(',')[9]:
                item['end_date'] = list.split(',')[9]
            else:
                item['end_date'] = None
            if list.split(',')[10]:
                item['danweijingzhi2'] = list.split(',')[10]
            else:
                item['danweijingzhi2'] = None
            if list.split(',')[11]:
                item['leijijingzhi2'] = list.split(',')[11]
            else:
                item['leijijingzhi2'] = None
            if list.split(',')[12]:
                item['create_date'] = list.split(',')[12]
            else:
                item['create_date'] = None
            if list.split(',')[14]:
                item['shouxufei'] = list.split(',')[14]
            else:
                item['shouxufei'] = None
            yield item




