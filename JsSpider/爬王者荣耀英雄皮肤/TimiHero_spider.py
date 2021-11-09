import os

from pyquery import PyQuery
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Cookie': 'pgv_pvid=4358581508; _ga=GA1.2.2088666116.1615622471; RK=LgjZD2cre+; ptcz=d6e186bfd50476b137990dfed20105c6218600ccc42ea70852975a0d20c539aa; tvfe_boss_uuid=ca8afa93a7196630; iip=0; pac_uid=1_1302897902; o_cookie=1302897902; LW_sid=N1A6Q3n2w0o3R8q3Q3X5q2w268; LW_uid=k1j6d3s2M0S3a8t3S345A2X372; eas_sid=p1y6M3G2v0a378p3t3j5J2s6F4; eas_entry=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DY3l3oauiBTWK3AoTkYimbG28E9gdQNq_YscS8J6N9fO%26wd%3D%26eqid%3Db9ca61bf00008ed9000000036146edb9; isHostDate=18889; PTTuserFirstTime=1632009600000; isOsSysDate=18889; PTTosSysFirstTime=1632009600000; isOsDate=18889; PTTosFirstTime=1632009600000; ts_refer=www.baidu.com/link; ts_uid=5074813880; weekloop=0-0-0-39; ied_qq=o1302897902; pt2gguin=o1302897902; ieg_ingame_userid=tefJKTBwcHilUQrS1XubDJUhOTQprfUq; ied_rf=--; pgv_info=ssid=s749733144&pgvReferrer=; pvpqqcomrouteLine=index_herolist_herodetail_herodetail_herodetail_herodetail_herodetail; ts_last=pvp.qq.com/web201605/herolist.shtml; PTTDate=1632040019699',
    'referer': 'https://pvp.qq.com/web201605/herolist.shtml'
}

url = "https://pvp.qq.com/web201605/herolist.shtml"

if not os.path.exists('./picture/'): # 王者荣耀英雄皮肤下载
    os.mkdir('./picture/')

if not os.path.exists('./WZskin_download/'): # 王者荣耀英雄皮肤下载
    os.mkdir('./WZskin_download/')

response = requests.get(url=url,headers=headers)
response.encoding = 'gbk'
# print(response.text)

# xpath解决问题
# dom_tree = etree.HTML(response.text)
# items = dom_tree.xpath('//ul[@class="herolist clearfix"]/li')
# # print(items)
# for item in items:
#     urls_list = item.xpath('./a/img/@src')
#     hero_name_list = item.xpath('./a/text()')
#     urls = ' '.join(urls_list)
#     hero_name = ' '.join(hero_name_list)
#     heropic_url = 'https:'+urls
#     with open('./WZskin_download/' + hero_name +'.jpg','wb') as f:
#         hero_pic = requests.get(heropic_url,headers=headers).content
#         f.write(hero_pic)
#     print("图片下载成功",hero_name)

# pyquery解决问题
html = response.content
doc = PyQuery(html)
items = doc(".herolist > li").items()
# print(items)
for item in items:
    url = item.find('img').attr('src')
    # print(url)
    urls = 'http:'+url
    name = item.find('a').text()
    # print(name)
    url_content = requests.get(url=urls,headers=headers).content
    with open('./picture/'+name+'.jpg','wb')as f:
        f.write(url_content)
        print("正在下载：%s.....%s" %(name,urls))
print("下载完毕！")
