# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import time
from .items import *
from .database_tool import DBConnector
from scrapy.exceptions import DropItem
from pymongo.errors import DuplicateKeyError

class ScrapyspidersPipeline:
    def process_item(self, item, spider):
        return item
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
