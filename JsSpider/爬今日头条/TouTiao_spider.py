import csv
import pandas as pd
import numpy
import requests
import pymysql
from lxml import etree

# file =open('今日头条.csv',mode='a',encoding='utf-8',newline='')
# csv_write = csv.DictWriter(file,fieldnames=['title','link','source','text','comment','create_time'])
# csv_write.writeheader()

def get_resp(url):
    headers = {
        'Cookie': '_S_DPR=1; _S_IPAD=0; MONITOR_WEB_ID=7019122699780146696; passport_csrf_token=27a861da23fd22abedf2807306533cd5; tt_webid=7019122699780146696; ttwid=1%7CPjfsNRBDvyALq7vUvHUoE0OpOEZG9kfHEs_Cfj5e928%7C1636606106%7C6f5b9a4feb49e5588f34a81fd5d0a203774e2980e53431124e9657538cc051b1; _S_WIN_WH=1920_936',
        'Host': 'so.toutiao.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    resp = requests.get(url=url,headers=headers).text
    return resp

def parse(html):
    html = etree.HTML(html)
    lists = html.xpath('//a[@class="text-ellipsis text-underline-hover"]')
    # print(lists)
    title_list = []
    link_list = []
    text_list = []
    source_list = []
    comment_num_list = []
    create_time_list = []
    for list in lists:
        title = list.xpath('./text()')
        title = str(title).replace('[','').replace("'","").replace(']','').replace(',','').strip()
        title_list.append(title)
        links = list.xpath('./@href')
        for link in links:
            link = 'https://so.toutiao.com/' + link
            link_list.append(link)

    sources = html.xpath('//span[@class="d-flex align-items-center text-ellipsis margin-right-4"]')
    for source in sources:
        source = source.xpath('./span[1]/text()')
        source = str(source).replace('[', '').replace("'", "").replace(']', '').replace(',', '').strip()
        source_list.append(source)


    comment_nums = html.xpath('//span[@class="text-ellipsis margin-right-4"]')
    for comment_num in comment_nums:
        comment_num = comment_num.xpath('./text()')
        comment_num = str(comment_num).replace('[', '').replace("'", "").replace(']', '').replace(',', '').strip()
        comment_num_list.append(comment_num)

    create_times = html.xpath('//div[@class="cs-view cs-view-flex align-items-center flex-row cs-source-content"]')
    for create_time in create_times:
        create_time = create_time.xpath('./span[3]/text()')
        create_time = str(create_time).replace('[', '').replace("'", "").replace(']', '').replace(',', '').strip()
        create_time_list.append(create_time)

    texts = html.xpath('//span[@class="text-underline-hover"]')
    for text in texts:
        text = text.xpath('./text()')
        text = str(text).replace('[', '').replace("'", "").replace(']', '').replace(',', '').strip()
        text_list.append(text)

    return title_list,link_list,source_list,comment_num_list,text_list,create_time_list

def save_csv(title_list,link_list,source_list,comment_num_list,text_list,create_time_list,i):
    head= ['title', 'link', 'source', 'comment_num', 'text', 'create_time']     #表头数据
    list = [title_list,link_list,source_list,comment_num_list,text_list,create_time_list]            #数据列表
    list_change = numpy.transpose(list)        #数据行列互换
    test = pd.DataFrame(columns=head, data=list_change)
    test.to_csv(rf'C:\CodeTime\JsSpider\爬今日头条\name_{i}.csv')

if __name__ == '__main__':
    for i in range(1,10):
        url = 'https://so.toutiao.com/search?keyword=%E7%96%AB%E6%83%85&pd=information&source=pagination&dvpf=pc&aid=4916&page_num={}&search_id=20211111124843010150132204497FB416'.format(i)
        html = get_resp(url)
        # print(html)
        title_list = parse(html)[0]
        link_list = parse(html)[1]
        source_list = parse(html)[2]
        comment_num_list = parse(html)[3]
        text_list = parse(html)[4]
        create_time_list = parse(html)[5]
        save_csv(title_list, link_list, source_list, comment_num_list, text_list, create_time_list,i)