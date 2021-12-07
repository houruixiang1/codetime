# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter
import time
import json
from .items import *
from .database_tool import DBConnector
from scrapy.exceptions import DropItem
from pymongo.errors import DuplicateKeyError

class ScrapyspidersPipeline(object):
    pass

class TTFundPipeline(object):
    def __init__(self):
        # python3保存文件 必须需要'wb'  保存为json格式
        self.f = open("itcast_pipeline.json", 'wb')

    def process_item(self, item, spider):
        # 读取item中的数据 并换行处理
        content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.f.write(content.encode('utf=8'))
        return item

    def close_spider(self, spider):
        # 关闭文件
        self.f.close()

class CeshiPipeline(object):

    def __init__(self):
        db_connector = DBConnector()
        self.db, self.client = db_connector.create_mongo_connection()

    def get_crawled_time(self):
        return time.strftime("%Y-%m-%d %H:%M:%S")

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        try:
            crawled_time = self.get_crawled_time()
            if isinstance(item, CeshiItem):
                post_id = item['id']
                item['crawled_time'] = crawled_time
                self.db['post'].update({"id": post_id}, {'$set': item},  upsert=True)
                return item

        except DuplicateKeyError:
            raise DropItem

