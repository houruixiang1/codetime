# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyspidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CeshiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    uu_id = scrapy.Field()
    title = scrapy.Field()
    source = scrapy.Field()
    text = scrapy.Field()
    id = scrapy.Field()
    created_at = scrapy.Field()
    text_url = scrapy.Field()
    belongsName = scrapy.Field()
    editor = scrapy.Field()
    crawled_time = scrapy.Field()  # 爬取时间
    hasImg = scrapy.Field()
    pics = scrapy.Field()
    video = scrapy.Field()
