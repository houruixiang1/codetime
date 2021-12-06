import json
import os
import sys
from pymongo import MongoClient
from service.utils_proiex import Proxy_pool
import requests
from requests import RequestException
from lxml import etree


# DIR_BASE = os.path.dirname(os.path.abspath(__file__)) + '/../..'
# os.chdir(DIR_BASE)
# sys.path.append(DIR_BASE)

class maoyan_rank_top100():

    def __init__(self):
        self.proxy_pool = Proxy_pool()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
            }
        self.Client = MongoClient()

    def crawl_one_page(self,url):
        try:
            response = self.proxy_pool.get_response(url=url, headers=self.headers)
            if response.status_code == 200:
                return response.text
            else:
                return None
        except RequestException:
            return False

    def parse(self,content):
        html = etree.HTML(content)
        # print(html)
        xpath_list = html.xpath('//dl[@class="board-wrapper"]/dd')
        movie_list = []
        for item in xpath_list:
            movie_dic = {}
            movie_name = item.xpath('./div/div/div[1]/p[1]/a/text()')[0]
            movie_name = str(movie_name).replace('[','').replace(']','').replace("'","").strip()
            movie_dic['movie_name'] = movie_name
            movie_score_1 = item.xpath('./div/div/div[2]/p/i[1]/text()')[0]
            movie_score_2 = item.xpath('./div/div/div[2]/p/i[2]/text()')[0]
            movie_dic['movie_score'] = float(str(movie_score_1) + str(movie_score_2))
            movie_list.append(movie_dic)
        return movie_list

    def parse_pagenum(self):
        urls = ['http://maoyan.com/board/4?offset={}'.format(i) for i in range(0,91,10)]
        return urls

    def write_in_file(self,data_list):
        for data in data_list:
            with open(r'./maoyan_top100.txt',mode='a',encoding='utf-8')as f:
                f.write(json.dumps(data, ensure_ascii=False) + '\n')

    def write_in_mongo(self, data_list):
        # print(data_list)
        db = self.Client.maoyan_ranktop100
        collection = db["maoyan_movie_top100"]
        for data in data_list:
            # print(data)
            datas = json.loads(data, ensure_ascii=False)
            collection.insert(datas)


if __name__ == '__main__':
    rank_top100 = maoyan_rank_top100()
    urls_list = rank_top100.parse_pagenum()
    for url in urls_list:
        # url = 'http://maoyan.com/board/4?offset=20'
        print("正在爬取{}".format(url))
        content = rank_top100.crawl_one_page(url)
        list_data = rank_top100.parse(content)
        # print(list_data)
        # rank_top100.write_in_file(list_data)
        rank_top100.write_in_mongo(list_data)
        print("已爬取完{}".format(url))
