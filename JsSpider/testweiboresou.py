# 微博同城数据月数据需求增加阅读量和评论量
import re
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import quote

from SameCityData import get_content
from yunjian_db import Yunjian_Db, MCODPS_Db

from utils import *

crawl_delay = 0.8


class SameCityData():
    proxies = {"http": "http://t11666754707153:qzgfe0ed@tps163.kdlapi.com:15818",
               "https": "http://t11666754707153:qzgfe0ed@tps163.kdlapi.com:15818"}
    # odps_db = MCODPS_Db(baseconf["odps_db"])
    # odps_db.set_log(log)
    filelist = []
    basepath = SAVE_BASEPATH
    content = ''

    hotsearch_beta = {
        "host":"rm-2zeusf532vs8v57tw9o.mysql.rds.aliyuncs.com",
        "user":"houruixiang",
        "passwd":"SESKd520dAf42",
        "name":"hotspot_beta",
    }

    hotsearchbeta_db = Yunjian_Db(hotsearch_beta)
    # hotsearchbeta_db.set_log(log)

    spider_database = {
        "host": "rm-bp1ypl73k40865d24qo.mysql.rds.aliyuncs.com",
        "user": "viki",
        "passwd": "99MKLd3h9i",
        "name": "viki_data",
    }
    spider_db = Yunjian_Db(spider_database)


    def get_cookie(self):
        sql = """
        SELECT cookies FROM cookies WHERE site = 'weibo_hotseach'
        """
        data = self.spider_db.select_data(sql)
        cookie = data[0]['cookies']
        return cookie

    def get_data(self):

        start_time, end_time = self.get_dt(1)
        sql = """
        SELECT * FROM `city_hotsearch_top` WHERE province =province and datetime>= '%s' AND datetime <= '%s' limit 1000
        """
        keywords = []
        all_records = []
        real_all_records = []
        keyword_datas = {}
        # for province in self.provinces:
        datasql = sql % (start_time, end_time)
        records = self.hotsearchbeta_db.select_data(datasql)
        # print(records)
        for record in records:
            keywords.append(record['keywords'])
            one = [record['datetime'], record['province'], record['city'], record['longitude'], record['latitude'], record['topnum'], record['keywords'], record['hotnum'],
                   record['hotflag'], record['url'], record['timestamp'], record['host']]
            all_records.append(one)
        keywords = list(set(keywords))
        # print(all_records)
        # return keywords
        for keyword in keywords:
            try:
                try:
                    # pool = ThreadPoolExecutor(max_workers=20)
                    # data = pool.submit(self.crawl_data,keyword)
                    # data=data.result()
                    data = self.crawl_data(keyword)
                except:
                    data = self.crawl_data(keyword, proxies=self.proxies)
            except:
                data = ''
            print(keyword, '阅读；讨论数', data)
            if data:
                keyword_datas[keyword] = data
            else:
                self.content += (keyword + ' ')
            time.sleep(crawl_delay)
            # break
        # pool.shutdown()
        rows = []
        sql = """insert into city_hotsearch_top_new(datetime, province, city, longitude, latitude, topnum, keywords, hotnum,
                                       hotflag, url, `timestamp`, host, `read`, comment) values"""
        for record in all_records:
            line = record.copy()
            keyword = record[6]
            if keyword in keyword_datas.keys():
                data = keyword_datas[record[6]]
                # print(keyword, data)
                read = data.split(';')[0]
                comment = data.split(';')[1]
            else:
                read = 0
                comment = 0
            keyword = quote(keyword)
            url = 'https://s.weibo.com/weibo?q=%23{}%23'.format(keyword)
            line.insert(12, read)
            line.insert(13, comment)
            # line.insert(9, url)

            # line = [record[0], read[1], record[2], str(record[3]), str(record[4]), str(read), str(comment), url, record[5], record[6]]
            # print(line)
            # real_all_records.append(line)
            rows.append("('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10],
                line[11], line[12], line[13]))
                # tup_list = tuple(list)
                # print(tup_list)
        self.hotsearchbeta_db.execute_sql_with_array(sql, "", rows)
        # print(rows)
        return rows

    def crawl_data(self, keyword, proxies=None):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
            'Cookie': 'SUB={}'.format(self.get_cookie())
        }
        keyword = quote(keyword)
        url = 'https://s.weibo.com/weibo?q=%23{}%23'.format(keyword)
        _, resp = get_content(url, headers=headers, proxies=proxies)
        try:
            read = re.search('<span>阅读(.*?)</span>', resp, re.S).group(1).strip()
            comment = re.search('<span>讨论(.*?)</span>', resp, re.S).group(1).strip()
        except:
            # print(resp)
            comment = ''
            read = ''
        if read and comment:
            if '亿' in read:
                read = int(float(read.replace('亿', '')) * 100000000)
            elif '万' in read:
                read = int(float(read.replace('万', '')) * 10000)
            else:
                read = int(float(read))

            if '亿' in comment:
                comment = int(float(comment.replace('亿', '')) * 100000000)
            elif '万' in comment:
                comment = int(float(comment.replace('万', '')) * 10000)
            else:
                comment = int(float(comment))
            data = str(read) + ';' + str(comment)
            return data
        else:
            return ''

    def main(self):
        lists = self.get_data()
        print(lists)
        # self.save_to_mysql(lists)

    def get_dt(self,n):
        today = datetime.datetime.now()
        # 计算偏移量
        offset = datetime.timedelta(days=-n)
        # 获取想要的日期的时间
        re_date = (today + offset).strftime('%Y-%m-%d')
        last_day_start = re_date + ' 00:00:00'
        last_day_start.format("")
        last_day_end = re_date + ' 23:59:59'
        return last_day_start, last_day_end

if __name__ == '__main__':
    task = SameCityData()
    task.main()

