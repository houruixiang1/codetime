import json
import re
import time

import jsonpath
import scrapy
from ..items import productItem
class JdShopSpider(scrapy.Spider):
    name = 'jd_shop'
    allowed_domains = ['jd.com','m.jd.com']
    # start_urls = ['http://jd.com/']

    def start_requests(self):
        sort = {
            'big_sort_name': '家用电器',
            'big_sort_url': 'https://jiadian.jd.com',
            'mid_sort_name': '电视',
            'mid_sort_url': 'https://list.jd.com/list.html?cat=737,794,798',
            'lit_sort_name': '全面屏电视',
            'lit_sort_url': 'https://list.jd.com/list.html?cat=737,794,798&ev=4155_97865&sort=sort_rank_asc&trans=1&JL=3_%E7%94%B5%E8%A7%86%E7%B1%BB%E5%9E%8B_%E5%85%A8%E9%9D%A2%E5%B1%8F#J_crumbsBar'
        }
        url = sort['lit_sort_url']
        yield scrapy.Request(url,callback=self.parse,meta={'item':sort})

    def parse(self, response):
        sort = response.meta['item']
        # print(response.text)
        # print(sort)
        result_list = response.xpath('//*[@id="J_goodsList"]/ul/li')
        for result in result_list:
            # print(result)
            item = productItem()
            sku_id = result.xpath('./@data-sku').extract()
            product_sku_id = str(sku_id).replace("[","").replace("]","").replace("'","").strip()
            # print(product_sku_id)
            item['product_sort'] = sort
            item['product_sku_id'] = product_sku_id
            product_url = 'https://cdnware.m.jd.com/c1/skuDetail/apple/7.3.0/{}.json'.format(item['product_sku_id'])
            yield scrapy.Request(product_url,callback=self.parse_product_base,meta={'item':item})

        url = sort['lit_sort_url']
        try_num = 0
        while try_num<3:
            next_page = re.search("s.init\((.*?), '",response.text,re.S).group(1).strip()
            # print(next_page)
            page = int(str(next_page.split(',')[0]).strip())
            num_page = int(str(next_page.split(',')[1]).strip())
            if page == 1:
                next_url = url.split('?')[0] + '?' + 'page={}&'.format(page + 1) + url.split('?')[1]
                # print(next_url)
                yield scrapy.Request(next_url, callback=self.parse, meta={'item': sort})
            else:
                if page < num_page:
                    next_url = url.split('?')[0] + '?' + 'page={}&'.format(page+1) + url.split('?')[1]
                    # print("ddddddddd",next_url)
                    yield scrapy.Request(next_url, callback=self.parse, meta={'item':sort})
            try_num+=1


    def parse_product_base(self,response):
        item = response.meta['item']
        # print(item)
        result = json.loads(response.text)
        # print(result)
        # 商品名称
        item['product_name'] = result['wareInfo']['basicInfo']['name']
        # 图书商品的信息
        item['product_book_info'] = result['wareInfo']['basicInfo']['bookInfo']
        # 商品图片url
        item['product_imageurl'] = result['wareInfo']['basicInfo']['wareImage'][0]['small']
        # 商品选项
        color_size = jsonpath.jsonpath(result,'$..colorSize')
        if color_size:
            color_size = color_size[0]
            if color_size:
                product_option = {}
                for option in color_size:
                    title = option['title']
                    value = jsonpath.jsonpath(option,'$..text')
                    product_option[title] = value
                item['product_option'] = product_option
        else:
            opt = {}
            opt['选项'] = '此商品没有选项'
            item['product_option'] = opt
        # 商品店铺
        shop = jsonpath.jsonpath(result,'$..shop')
        if shop:
            shop = shop[0]
            if shop:
                shopinfo = {
                    'shopId' : shop['shopId'],
                    'shopname': shop['name'],
                    'shopscore': shop['score']
                }
            else:
                shopinfo = {
                    'shopname': '京东自营'
                }
            item['product_shopinfo'] = shopinfo
        product_sort_id = result['wareInfo']['basicInfo']['category']
        item['product_sort_id'] = product_sort_id.replace(";",",")
        yield item