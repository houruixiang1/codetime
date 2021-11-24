import re

import requests
from lxml import etree

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

    def handel_detail_rank(self,url):
        rank_list = []
        resp = self.handel_requests(url)
        # print(resp)
        html = etree.HTML(resp)
        rank_list_xpath = html.xpath('/html/body/div[2]/div[2]/div/div/div[2]/div[@class="BOOKLIST"]')
        for rank in rank_list_xpath:
            rank_name = rank.xpath('./p[@class="bookName"]/a/text()')
            rank_url = rank.xpath('./p[@class="bookName"]/a/@href')
            # print(rank_name,rank_url)
            rank_list.append({'rank_name': rank_name, 'rank_url': rank_url})
        # print("-----------------------------------------------------------------")
        return rank_list


    def handel_zhangjies(self,url):
        zhangjie_list = []
        resp = self.handel_requests(url)
        html = etree.HTML(resp)
        zhangjie_list_xpath = html.xpath('/html/body/div[3]/div[1]/div[3]/dl[1]/dd/a')
        for i,zhangjie in enumerate(zhangjie_list_xpath):
            if(i<=19):
                zhangjie_name = zhangjie.xpath('./span/text()')
                zhangjie_url = zhangjie.xpath('./@href')
                # print(zhangjie_name,zhangjie_url)
                zhangjie_list.append({"zhangjie_name":zhangjie_name,"zhangjie_url":zhangjie_url})
            else:
                break
            # print("--------------------------------------------------")
        return zhangjie_list

    def handel_detail_zhangjie(self,urls):
        xiaoshuo_data = []
        # i_list = []
        # for name in names:
        #     print(name[0].replace('[','').replace(']','').replace("'","").strip())
        for i,url in enumerate(urls):
            # i_list.append(i)
            real_xiaoshuo_zhangjie_url = 'https://www.4yt.net' + url
            resp = self.handel_requests(real_xiaoshuo_zhangjie_url)
            html = etree.HTML(resp)
            zhangjie_list_xpath = html.xpath('/html/body/div[2]/div/div[3]/p/text()')

            xiaoshuo_data.append(zhangjie_list_xpath)
            print("已存入%s章" % i)
        # for i in i_list:
        real_data = str(xiaoshuo_data).replace('[','').replace(']','').replace("'","").replace('本书首发来自','').replace('，第一时间看正版内容！','').strip()
        with open(r'C:\CodeTime\txt' + str(i)+'.txt', mode='a', encoding='utf-8')as f:
            f.write(real_data)
        # print(str(xiaoshuo_data))
        # return xiaoshuo_data
    def main(self):
        content = self.handel_requests(self.start_url)
        # print(content)
        ranks = self.handel_rank(content)
        # print(ranks)
        name_list = []
        url_list = []
        for i,rank in enumerate(ranks):
            # print(i)
            urls = rank['rank_url']
            for url in urls:
                real_rank_url = 'https://www.4yt.net'+url
                xiaoshuo_ranks = self.handel_detail_rank(real_rank_url)
                # print(xiaoshuo_ranks)
                for i, xiaoshuo_rank in enumerate(xiaoshuo_ranks):
                    # print(i)
                    urls = xiaoshuo_rank['rank_url']
                    names = xiaoshuo_rank['rank_name']
                    # print(names)
                    name_list.append(names)
                    for url in urls:
                        real_xiaoshuo_rank_url = 'https://www.4yt.net' + url
                        # print(real_xiaoshuo_rank_url)
                        xiaoshuo_zhangjies = self.handel_zhangjies(real_xiaoshuo_rank_url)
                        # print(xiaoshuo_zhangjies)
                        for i, xiaoshuo_zhangjie in enumerate(xiaoshuo_zhangjies):
                            urls = xiaoshuo_zhangjie['zhangjie_url']
                            # url_list.append(urls)
                            # names = xiaoshuo_zhangjie['zhangjie_name']
                            self.handel_detail_zhangjie(urls)
                            # print(zhangjie_detail_text)
        # print(name_list)



if __name__ == '__main__':
    task = book()
    task.main()