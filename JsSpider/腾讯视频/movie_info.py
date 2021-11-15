import time

print(
    '''
 排序  sort   最近热播：18，最新上架：19，高分好评：21，知乎高分：22
 类型  itype  全部：-1，剧情:100018，喜剧:100004，动作:100061，爱情:100005，惊悚:100010，犯罪:4，悬疑:100009，战争:100006，科幻:100012，动画:100015，恐怖:100007，
        家庭:100017，传记:100022，冒险:100003，奇幻:100016，武侠:100011，历史:100021，运动:2，歌舞:100014，音乐:100013，纪录：100020，伦理:100019，西部：3
 特色  characteristic  全部:-1，院线:1，自制电影:2，独播:5，原声:8，粤语:9，蓝光:3，奥斯卡:6
 地区  iarea  全部:-1，内地:100024，中国香港:100025，美国:100029，欧洲:100032，中国台湾:100026，日本:100027，韩国:100028，印度:100030，泰国:100031，英国:15，法国:16，
        德国:17，加拿大:18，西班牙:19，意大利:20，澳大利亚:21，北欧:22，拉丁美洲:23，其它:100033
 年份  year  全部：-1,2021:2021,2020:2020,2019:2019,2018:2018,2017:2017,2016:2016,2015:100063,2014:100034，2013-2011:100035，2010-2006:100036，2005-2000:100037，90年代:100038，80年代:100039，其它:100040
 资费  charge  全部：-1，免费：1，包月：2，用券：3，付费：4 
 '''
)
import requests
import re
from bs4 import BeautifulSoup
import csv

def requests_page(characteristic,charge,iarea,itype,sort,year,page):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'referer': 'https://v.qq.com/channel/movie',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    url = 'https://v.qq.com/x/bu/pagesheet/list?_all=1&append=1&channel=movie&characteristic={}&charge={}&iarea={}&itype={}&listpage=2&offset={}&pagesize=30&sort={}&year={}'.format(characteristic, charge, iarea, itype, page, sort, year)
    # data = {
    #     '_all': 1,
    #     'append': 1,
    #     'channel': 'movie',
    #     'characteristic': characteristic,
    #     'charge': charge,
    #     'iarea': iarea,
    #     'itype': itype,
    #     'listpage': 2,
    #     'offset': 30,
    #     'pagesize': 30,
    #     'sort': sort,
    #     'year': year
    # }
    resp = requests.get(url,headers=headers)
    resp.encoding='utf-8'
    # print(resp.text)
    return resp.text

def parse(resp):
    bs = BeautifulSoup(resp,'html.parser')
    result1 = bs.find_all("div",class_="list_item")
    # print(result1)
    list = []
    for res in result1:
        # print(type(res))
        if 'figure_title figure_title_two_row bold' in str(res):
            result2 = res.find("a",class_="figure_title figure_title_two_row bold")
            # print(result2)
            title = result2.text
            text_link = result2.get("href")
        else:
            title = None
            text_link = None

        if 'figure_caption' in str(res):
            result3 = res.find("img", class_="figure_pic")
            pic_link = 'https:' + result3.get("src")
        else:
            pic_link = None

        if 'figure_caption' in str(res):
            result4 = res.find("div", class_="figure_caption")
            time_length = result4.text
        else:
            time_length = None
        if 'figure_score' in str(res):
            result5 = res.find("div", class_="figure_score")
            score = result5.text
        else:
            score = None
        # print(time_length,score)
        if 'figure_desc' in str(res):
            result6 = res.find("div", class_="figure_desc")
            desc = result6.text
        else:
            desc = None
        if 'figure_count' in str(res):
            result7 = res.find("div", class_="figure_count")
            play_count = result7.text
        else:
            play_count = None
        # print(title,text_link,pic_link,time_length,score,desc,play_count)
        list.append((title,text_link,pic_link,time_length,score,desc,play_count))
    return list

def save_csv(list_data):
    # file =open('腾讯视频电影分类信息.csv',mode='a',encoding='utf-8',newline='')
    # csv_write = csv.DictWriter(file,fieldnames=['title','text_link','pic_link','time_length','score','desc','play_count'])
    # csv_write.writeheader()
    with open(r'C:\CodeTime\JsSpider\腾讯视频\tencent.csv', 'a', newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for row in list_data:
            writer.writerow(row)
        print("所有的文件都已写入完毕！")
        csvfile.close()
if __name__ == '__main__':
    # lists = ['characteristic','charge','iarea','itype','sort','year']
    # for list in lists:
    characteristic = input("输入特色：")
    charge = input("输入资费：")
    iarea = input("输入地区：")
    itype = input("输入类型：")
    sort = input("输入排序：")
    year = input("输入年份：")
    # page = 30
    print("输入页数(默认前120)")
    time.sleep(2)
    i = 0
    while(1):
        if i==3000:
            break
        page = i
        i = i+30
        print(page)
        resp= requests_page(characteristic,charge,iarea,itype,sort,year,page)
        list_data = parse(resp)
        save_csv(list_data)


