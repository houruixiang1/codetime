# 快速更新b站数据，多线程
import numpy
import time
import pymysql
import logging
import threading
import operator

import requests
# proxies = {"http": "http://t13227749450836:beluyzjo@tps191.kdlapi.com:15818", "https": "https://t13227749450836:beluyzjo@tps191.kdlapi.com:15818"}


def get_ups_name(mid):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }
    url = 'https://api.bilibili.com/x/space/acc/info?mid=%s&jsonp=jsonp'%(str(mid))
    resp = requests.get(url, headers=headers,verify=False).json()
    name = resp['data']['name']
    cred = resp['data']['official']['title']
    return (name,cred)

def get_follower_count(mid):
    # 获取up粉丝数量
    headers = {
        'Host': 'api.bilibili.com',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Referer': 'https://space.bilibili.com/%s'%(str(mid)),
    }
    url = 'https://api.bilibili.com/x/relation/stat?vmid=%s'%(str(mid))
    info = requests.get(url, headers=headers,verify=False).json()
    follower_count = info['data']['follower']
    return follower_count

def get_likes_count(mid):
    headers = {
        'Host': 'api.bilibili.com',
        'Origin': 'https://space.bilibili.com',
        'Connection': 'keep-alive',
        'Cookie': "SESSDATA=1aee0fd3%2C1650698894%2C010cb%2Aa1;",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Referer': 'https://space.bilibili.com/%s'%(str(mid)),
    }
    url = 'https://api.bilibili.com/x/space/upstat?mid=%s&jsonp=jsonp' % (str(mid))
    info = requests.get(url, headers=headers, verify=False).json()
    likes_count = info['data']['likes']
    return likes_count

def get_contribute_count(mid):
    # 得到b站博主的投稿数 = 视频数 + 书刊数 + 音频数 + 图片数
    pass



if __name__ == '__main__':
    print(get_ups_name(1131457022))
    print(get_follower_count(1131457022))
    print(get_likes_count(1131457022))
    print(get_contribute_count(1131457022))
    # crawl_threads(1, threads_count=5)
    # 旧版启动
    # for group_id in GROUP_IDS:
    #     print(group_id)
    #     crawl_threads(group_id,threads_count=2)
    #     time.sleep(2)