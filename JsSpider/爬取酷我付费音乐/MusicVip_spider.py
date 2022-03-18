import os
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'csrf': '7LJGOB9C999',
    'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1632022449; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1632022449; _ga=GA1.2.785177090.1632022450; _gid=GA1.2.715131973.1632022450; kw_token=7LJGOB9C999',
    'Referer': 'http://kuwo.cn/search/list'
}
search_music = input("请输入一首歌的歌名或人名：")
url = "http://kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn=1&rn=30&httpsStatus=1&reqId=74ec1690-18fb-11ec-8f2f-27222b47caa2".\
    format(search_music)

if not os.path.exists('./KWmusicVip_download/'):
    os.mkdir('./KWmusicVip_download/')

response = requests.get(url=url,headers=headers)
response_data = response.json()
detail_data = response_data['data']['list']
# print(detail_data)
for i in detail_data:
    music_name = i['name']
    music_rid = i['rid']
    print(music_name,music_rid)
    Vipurl = "http://kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3&br=128kmp3&from=web&t=1632022881917&httpsStatus=1&reqId=74ecb2d1-18fb-11ec-8f2f-27222b47caa2".format(music_rid)
    music_url = requests.get(url=Vipurl,headers=headers).json()['url']
    with open('./KWmusicVip_download/'+music_name+'.mp3','wb') as f:
        mp3_download = requests.get(url=music_url,headers=headers).content
        f.write(mp3_download)
    print('下载成功',music_name)








