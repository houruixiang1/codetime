import re
import requests
import csv

url="https://dytt89.com/"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

response = requests.get(url=url,headers=headers)
response.encoding='gb2312'
# print(response.text)
opt = re.compile(r'2021必看热片.*?<ul>(?P<ul>.*?)</ul>',re.S)
opt1 = re.compile(r"href='(?P<movie_link>.*?)' title=",re.S)
opt2 = re.compile(r'◎译　　名(?P<movie_name>.*?)<br />'
                  r'.*?<div class=player_list>.*?<a href="(?P<movie_download>.*?)">',re.S)
iters = opt.finditer(response.text)
movie_links=[]
for iter in iters:
    ul = iter.group('ul').strip()
    iters=opt1.finditer(ul)
    for iter in iters:
        movie_link = 'https://dytt89.com'+iter.group('movie_link')
        movie_links.append(movie_link)
for link in movie_links:
    # print(link)
    resp = requests.get(url=link, headers=headers)
    resp.encoding='gb2312'
    movie_downloads = opt2.finditer(resp.text)
    for movie_download in movie_downloads:
        print(movie_download.group('movie_name'))
        print(movie_download.group('movie_download'))



