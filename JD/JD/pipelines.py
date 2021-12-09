# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from .settings import MONGODB_URL
from .spiders.jd_sort import JdSortSpider
from pymongo import MongoClient

class Jd_SortPipeline(object):
    def open_spider(self,spider):
        if isinstance(spider, JdSortSpider):
            self.mongo = MongoClient(MONGODB_URL)
            self.collection = self.mongo['jd']['sort']

    def process_item(self, item, spider):
        if isinstance(spider, JdSortSpider):
            self.collection.insert_one(dict(item))
        return item

    def close_spider(self,spider):
        if isinstance(spider, JdSortSpider):
            self.mongo.close()