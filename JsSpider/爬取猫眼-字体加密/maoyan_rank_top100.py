import json
import os
import sys
import time
from pymongo import MongoClient
import requests
from requests import RequestException
from lxml import etree
from selenium import webdriver
from selenium.webdriver import ActionChains


class maoyan_rank_top100():

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
            }
        self.Client = MongoClient()
    # 爬取猫眼网页内容，猫眼对IP的校验挺严的，大概三五次就得进行验证
    # 想法：使用selenium进行模拟验证登陆，滑块验证（未实现），需要计算滑块到缺口的位置。
    def crawl_one_page(self,url):
        try:
            response = requests.get(url=url, headers=self.headers)
            if response.status_code == 200 and '猫眼验证中心' not in response.text:
                return response.text
            elif response.status_code == 200 and '猫眼验证中心' in response.text:
                options = webdriver.ChromeOptions()
                # options.add_argument('--headless')
                options.add_argument(
                    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36')
                options.add_argument('--no-sandbox')
                options.add_argument('window-size=1920x3000')
                options.add_argument('--disable-gpu')
                options.add_argument('--disable-blink-features=AutomationControlled')

                driver = webdriver.Chrome(options=options)
                # print(k, v)
                driver.get(url)
                driver.maximize_window()
                time.sleep(5)
                return driver.page_source
            else:
                return None
        except RequestException:
            return False

    # 使用xpath解析数据
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

    # 构造url
    def parse_pagenum(self):
        urls = ['http://maoyan.com/board/4?offset={}'.format(i) for i in range(0,91,10)]
        return urls

    # 写入txt文件
    def write_in_file(self,data_list):
        for data in data_list:
            with open(r'./maoyan_top100.txt',mode='a',encoding='utf-8')as f:
                f.write(json.dumps(data, ensure_ascii=False) + '\n')

    # 写入mongodb
    def write_in_mongo(self, data_list):
        # print(data_list)
        db = self.Client.maoyan_ranktop100
        collection = db["maoyan_movie_top100"]
        for data in data_list:
            # print(data)
            # datas = json.dumps(data, ensure_ascii=False)
            collection.insert_one(data)

# 主程序运行
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
