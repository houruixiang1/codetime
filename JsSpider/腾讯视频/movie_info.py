import requests
import re

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    # cache-control: max-age=0
    # cookie: RK=4gjZD0cqN8; ptcz=968e256e0ed1449a8edf7eb552eb0d1e48f729b5d730e17df018ebf3257befcf; tvfe_boss_uuid=e270318620bfae78; video_guid=6531aa1712fcb214; video_platform=2; pgv_pvid=4817638682; ts_uid=5898137536; bucket_id=9231007; eas_sid=81E6g3A4p5J4u140360596N0U8; ts_refer=www.baidu.com/link; fqm_pvqid=b3a2bb1f-e7bd-4dc2-84e7-7ae9dd65b7e6; euin=oKozowcq7iEzoc**; wxopenid=; psrf_qqrefresh_token=CF43928D3DB15064F82AAEAD7CB9B4B6; wxrefresh_token=; psrf_access_token_expiresAt=1642401586; psrf_qqunionid=A7B0F9DA3AC08A46820D17DF821BB167; tmeLoginType=2; wxunionid=; psrf_qqaccess_token=F160A68E94DD20698F172A02582BBA06; psrf_qqopenid=B7E8042C5E4A78C5882B76FF480B64BC; sd_userid=21901634806712044; sd_cookie_crttime=1634806712044; _qpsvr_localtk=0.9191732146970362; ptui_loginuin=1302897902@qq.com; pgv_info=ssid=s7983206580; login_remember=qq; main_login=qq; vqq_vusession=31zTOzgbWwUxT_gob4W-CA..; vqq_vuserid=1236286095; vqq_appid=101483052; vqq_openid=2F6AD981CB46B69978205F71FC331494; vqq_access_token=BB2D5367AFEAC2688AED71FB1A4D548C; qq_nick=%E6%97%B6%E5%85%89%E4%BE%9D%E6%97%A7%E8%93%9D; qq_head=http://thirdqq.qlogo.cn/g?b=sdk&k=5DQo7ibiakxg3Yj7W2ibmI4pw&s=140&t=1554354284; lw_nick=%E6%97%B6%E5%85%89%E4%BE%9D%E6%97%A7%E8%93%9D|0|http://thirdqq.qlogo.cn/g?b=sdk&k=5DQo7ibiakxg3Yj7W2ibmI4pw&s=140&t=1554354284|0; uid=984433300; ts_last=v.qq.com/channel/movie; qv_als=STYvi1IwPRJ8HipkA116369443126Rkh0A==; ptag=www_baidu_com|channel; ad_play_index=32
    'referer': 'https://v.qq.com/channel/movie',
    # sec-ch-ua: "Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"
    # sec-ch-ua-mobile: ?0
    # sec-ch-ua-platform: "Windows"
    # sec-fetch-dest: document
    # sec-fetch-mode: navigate
    # sec-fetch-site: same-origin
    # sec-fetch-user: ?1
    # upgrade-insecure-requests: 1
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}
url = 'https://v.qq.com/x/bu/pagesheet/list?'
#  sort   最近热播：18，最新上架：19，高分好评：21，知乎高分：22
#  itype  全部：-1，剧情:100018，喜剧:100004，动作:100061，爱情:100005，惊悚:100010，犯罪:4，悬疑:100009，战争:100006，科幻:100012，动画:100015，恐怖:100007，
#         家庭:100017，传记:100022，冒险:100003，奇幻:100016，武侠:100011，历史:100021，运动:2，歌舞:100014，音乐:100013，纪录：100020，伦理:100019，西部：3
#  characteristic  全部:-1，院线:1，自制电影:2，独播:5，原声:8，粤语:9，蓝光:3，奥斯卡:6
#  iarea  全部:-1，内地:100024，中国香港:100025，美国:100029，欧洲:100032，中国台湾:100026，日本:100027，韩国:100028，印度:100030，泰国:100031，英国:15，法国:16，
#         德国:17，加拿大:18，西班牙:19，意大利:20，澳大利亚:21，北欧:22，拉丁美洲:23，其它:100033
#  year  全部：-1,2021:2021,2020:2020,2019:2019,2018:2018,2017:2017,2016:2016,2015:100063,2014:100034，2013-2011:100035，2010-2006:100036，2005-2000:100037，90年代:100038，80年代:100039，其它:100040
#  charge  全部：-1，免费：1，包月：2，用券：3，付费：4

data = {
    '_all': 1,
    'append': 1,
    'channel': 'movie',
    'characteristic': -1,
    'charge': -1,
    'iarea': -1,
    'itype': -1,
    'listpage': 2,
    'offset': 30,
    'pagesize': 30,
    'sort': 18,
    'year': -1
}
resp = requests.get(url,headers=headers,data=data)
resp.encoding='utf-8'
print(resp.text)
