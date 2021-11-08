import scrapy


class TestbaiduSpider(scrapy.Spider):
    name = 'testbaidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        title = response.xpath('//*[@id="s-top-left"]/a[3]/text()').extract()
        print(title)