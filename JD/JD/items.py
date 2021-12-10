# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class productItem(scrapy.Item):
    # 商品分来
    product_sort = scrapy.Field()
    # 商品sku_id值，用于进入商品的详情页面
    product_sku_id = scrapy.Field()
    # 商品名称
    product_name = scrapy.Field()
    # 图书信息，只对图书商品的某个套装有用
    product_book_info = scrapy.Field()
    # 商品图片的url
    product_imageurl = scrapy.Field()
    # 商品选项，如：大小、尺寸、颜色等
    product_option = scrapy.Field()
    # 商品的分类id、用于获取评论、价格等信息
    product_sort_id = scrapy.Field()
    # 商品店铺信息（包含店铺id、店铺名称、店铺评分）
    product_shopinfo = scrapy.Field()
    # 商品价格
    product_price = scrapy.Field()
    # 商品评价信息
    product_score = scrapy.Field()


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
