import csv
import json
import logging
import os
import re
from ast import literal_eval
from distutils.util import strtobool

import redis
import requests
import scrapy
from scrapy.utils.project import get_project_settings
from scrapy_redis.spiders import RedisSpider


class TtfundSpider(RedisSpider):
    name = 'TTFund'
    allowed_domains = ['fund.eastmoney.com']
    # start_urls = ['http://fund.eastmoney.com/']
    redis_key = 'TTFund:start_urls'


    def __init__(self,  node='master', uu_id='000000002021', schedule='False', *args, **kwargs):
        super(TtfundSpider, self).__init__(*args, **kwargs)
        self.__task_id = uu_id
        # self.keywords = list(filter(None, keyword.split('|')))
        # self.operation = operation
        self.redis_key = self.redis_key + "_" + uu_id
        self.node = node
        file = open(r'C:\CodeTime\csv\自定义基金排行.csv', mode='a', encoding='utf-8', newline='')
        csv_write = csv.DictWriter(file,fieldnames=['股票代码', '股票名称', '股票涨幅', '股票分红', '股票分红次数',
                                                '股票开始日期', '股票单位净值1', '股票累计净值1','股票累计净值1',
                                                '股票结束日期', '股票单位净值2', '股票累计净值2', '股票创建日期',
                                                    '股票手续费'])
        csv_write.writeheader()
        self.csv_write = csv_write
        self.schedule = strtobool(schedule)

        if not os.path.exists('/data/'):
            os.makedirs('/data/')

        if node == 'master':
            settings = get_project_settings()
            r = redis.Redis(host=settings.get("REDIS_HOST"), port=settings.get("REDIS_PORT"), decode_responses=True)
            for i in range(0,10):
                url = 'http://fund.eastmoney.com/data/rankhandler.aspx?op=dy&dt=kf&ft=all&rs=&gs=0&sc=qjzf&st=desc&sd=2020-11-22&ed=2021-11-22&es=0&qdii=&pi={}&pn=50&dx=0'.format(i)
                request_data = {
                    'url': url,
                }
                r.lpush(self.redis_key,json.dumps(request_data))  # 1.r.lpush列表  2.字典转换为字符串
            # print(r.lrange(self.redis_key,0,1))

    def make_request_from_data(self, data):
        data = json.loads(data)  #字符串转换为字典
        # print("hello",data)
        url = data.get('url')
        # meta = data.get('meta')
        # # print(meta['key_words'])
        # # print(meta['page'])
        # print("Fetch url:", url)
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
        return int(page_num)

    def parse(self, response):
        resp = response.text
        if '-999' in resp:
            return None
        data = re.search('var rankData = .*?(\[.*?\])',resp,re.S).group(1).strip()
        lists = literal_eval(data)
        data_dict = {}
        for list in lists:
            # print(list)
            code = list.split(',')[0]
            name = list.split(',')[1]
            zhangfu = list.split(',')[3]
            fenhong = list.split(',')[4]
            fenhong_num = list.split(',')[5]
            start_date = list.split(',')[6]
            danweijingzhi1 = list.split(',')[7]
            leijijingzhi1 = list.split(',')[8]
            end_date = list.split(',')[9]
            danweijingzhi2 = list.split(',')[10]
            leijijingzhi2 = list.split(',')[11]
            create_date = list.split(',')[12]
            shouxufei = list.split(',')[14]
            data_dict = {"股票代码": code,"股票名称": name,"股票涨幅": zhangfu,"股票分红": fenhong,"股票分红次数": fenhong_num,"股票开始日期": start_date,
                         "股票单位净值1": danweijingzhi1,"股票累计净值1": leijijingzhi1,"股票结束日期": end_date,"股票单位净值2": danweijingzhi2,"股票累计净值2": leijijingzhi2,
                         "股票创建日期": create_date, "股票手续费": shouxufei}
            self.csv_write.writerow(data_dict)
        print("所有的文件都已保存进入csv！！！")



