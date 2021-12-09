import json

import scrapy

from ..items import sortItem


class JdSortSpider(scrapy.Spider):
    name = 'jd_sort'
    allowed_domains = ['3.cn']
    # https://dc.3.cn/category/get
    start_urls = ['https://dc.3.cn/category/get']

    def parse(self, response):
        content = json.loads(response.text)
        results = content['data']

        for result in results:
            item = sortItem()
            big_sort = result['s'][0]
            big_sort_info = big_sort['n']
            # print('大分类：{}'.format(big_sort_info))
            item['big_sort_name'],item['big_sort_url'] = self.parse_sort(big_sort_info)
            for mid_sort in big_sort['s']:
                mid_sort_info = mid_sort['n']
                # print('中分类：{}'.format(mid_sort_info))
                item['mid_sort_name'], item['mid_sort_url'] = self.parse_sort(mid_sort_info)
                for lit_sort in mid_sort['s']:
                    lit_sort_info = lit_sort['n']
                    # print('小分类：{}'.format(lit_sort_info))
                    item['lit_sort_name'], item['lit_sort_url'] = self.parse_sort(lit_sort_info)

                    yield item

    def parse_sort(self,data):
        name = data.split('|')[1]
        da = data.split('|')[0]
        if da.count('jd.com') == 1:
            url = 'https://' + da
        elif da.count('-') == 2:
            xx = da.replace('-',',')
            url = 'https://list.jd.com/list.html?cat={}'.format(xx)
        else:
            url = 'https://channel.jd.com/{}.html'.format(da)
        return name,url