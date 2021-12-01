import os
import re
from multiprocessing import Queue
from concurrent.futures import ThreadPoolExecutor
import requests
from lxml import etree
queue = Queue()
class book(object):
    def __init__(self):
        self.start_url = 'https://www.4yt.net/top/'
        self.haeders = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
        }

    def handel_requests(self,url):
        resp = requests.get(url = url, headers = self.haeders)
        resp.encoding='utf-8'
        resp = resp.text
        return resp

    def handel_rank(self,content):
        rank_list = []
        html = etree.HTML(content)
        rank_list_xpath = html.xpath('//div[@class="Main"]/div[@class="Left"]/ul[@class="list"]/li')
        for rank in rank_list_xpath:
            rank_name = rank.xpath('./a/span/text()')
            if '全部' in str(rank_name):
                continue
            else:
                rank_url = rank.xpath('./a/@href')
            rank_list.append({'rank_name':rank_name,'rank_url':rank_url})
            # print(rank_name,rank_url)
        return rank_list

    def handel_detail_rank(self,url,name):
        if not os.path.exists('./{}/'.format(name)):
            os.mkdir('./{}/'.format(name))
        resp = self.handel_requests(url)
        html = etree.HTML(resp)
        rank_list_xpath = html.xpath('/html/body/div[2]/div[2]/div/div/div[2]/div[@class="BOOKLIST"]')
        rank_list = []
        # rank_dict = {}
        for rank in rank_list_xpath:
            rank_dict = {}
            rank_name1 = rank.xpath('./p[@class="bookName"]/a/text()')
            rank_name = str(rank_name1).replace('[', '').replace(']', '').replace("'", "").strip()
            rank_url1 = rank.xpath('./p[@class="bookName"]/a/@href')
            rank_url = str(rank_url1).replace('[', '').replace(']', '').replace("'", "").strip()
            rank_dict['rank_name'] = rank_name
            rank_dict['rank_url'] = rank_url
            rank_list.append(rank_dict)
        return rank_list

    def handel_queue(self):
        pool = ThreadPoolExecutor(max_workers=4)
        while queue.qsize()>0:
            pool.submit(self.handel_zhangjies,queue.get())

    def handel_zhangjies(self,list,name):
        zhangjie_list = []
        for dict in list:
            # print(dict,name)
            zhangjie_dict = dict
            zhangjie_name = zhangjie_dict['rank_name']
            if not os.path.exists('C:\\CodeTime\\JsSpider\\爬17k小说\\多线程-九个榜单\\{}\\{}\\'.format(name,zhangjie_name)):
                os.mkdir('C:\\CodeTime\\JsSpider\\爬17k小说\\多线程-九个榜单\\{}\\{}\\'.format(name,zhangjie_name))
            url = zhangjie_dict['rank_url']
            zhangjie_url = 'https://www.4yt.net' + url
            resp = self.handel_requests(zhangjie_url)
            html = etree.HTML(resp)
            zhangjie_list_xpath = html.xpath('/html/body/div[3]/div[1]/div[3]/dl[1]/dd/a')
            for i,zhangjie in enumerate(zhangjie_list_xpath):
                if(i<=3):
                    zhangjie_dict = {}
                    zhangjie_name = zhangjie.xpath('./span/text()')
                    zhangjie_detail_name = zhangjie_name[0].strip()
                    zhangjie_url_1 = zhangjie.xpath('./@href')
                    zhangjie_detail_url = str(zhangjie_url_1).replace('[', '').replace(']', '').replace("'", "").strip()
                    # print(zhangjie_detail_name,zhangjie_detail_url)
                    zhangjie_dict['zhangjie_name'] = zhangjie_detail_name
                    zhangjie_dict['zhangjie_url'] = zhangjie_detail_url
                    zhangjie_list.append(zhangjie_dict)
                else:
                    break
            # print("--------------------------------------------------")
        return zhangjie_list

    def handel_detail_zhangjie(self,urls):
        # xiaoshuo_name = str(name).replace('[','').replace(']','').replace("'","").strip()
        # print("开始保存小说[%s]前20章！！！" % xiaoshuo_name)
        # xiaoshuo_datas = []
        for url in urls:
            real_xiaoshuo_zhangjie_url = 'https://www.4yt.net' + url
            print(real_xiaoshuo_zhangjie_url)
            # resp = self.handel_requests(real_xiaoshuo_zhangjie_url)
            # html = etree.HTML(resp)
            # zhangjie_list_xpath = html.xpath('/html/body/div[2]/div/div[3]/p/text()')
            # real_data = str(zhangjie_list_xpath).replace('[','').replace(']','').replace("'","").replace('本书首发来自','').replace('，第一时间看正版内容！','').strip()
            # with open(r'C:\CodeTime\txt\\'+xiaoshuo_name+'.txt', mode='a', encoding='utf-8')as f:
            #     f.write(real_data+'\r\n')
                # f.write('\r\n')
                # f.close()
        # print("小说【%s】前20章保存完毕！！！" % xiaoshuo_name)
    def main(self):
        content = self.handel_requests(self.start_url)
        ranks = self.handel_rank(content)
        xiaoshuo_names_list = []
        xiaoshuo_zhangjie_list = []
        for rank in ranks:
            urls = rank['rank_url']
            names = rank['rank_name']
            for i,url in enumerate(urls):
                real_rank_url = 'https://www.4yt.net'+url
                xiaoshuo_ranks = self.handel_detail_rank(real_rank_url, names[i])
                for xiaoshuo_rank in xiaoshuo_ranks:
                    xiaoshuo_names_list.append(xiaoshuo_rank['rank_name'])
                xiaoshuo_mulus = self.handel_zhangjies(xiaoshuo_ranks,names[i])
                print(xiaoshuo_mulus)





if __name__ == '__main__':
    task = book()
    task.main()