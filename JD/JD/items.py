# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class sortItem(scrapy.Item):
    # 大分类名字
    big_sort_name = scrapy.Field()
    # 大分类url
    big_sort_url = scrapy.Field()
    # 中分类名字
    mid_sort_name = scrapy.Field()
    # 中分类url
    mid_sort_url = scrapy.Field()
    # 小分类名字
    lit_sort_name = scrapy.Field()
    # 小分类url
    lit_sort_url = scrapy.Field()
