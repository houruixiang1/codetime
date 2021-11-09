import threading
import time
import urllib.request

def surf_net(url):
    start_time = time.time()
    print("surf start",start_time)
    try:
        urllib.request.urlopen(url)
    except urllib.URLError as e:
        print(e.reason)
    time.sleep(2)
    end_time = time.time()
    print(url,urllib.request.urlopen(url).code,end_time-start_time)
url_list =['https://www.taobao.com','https://www.baidu.com','https://www.jd.com']
for j in url_list:
    print(j)
    surf_net(j)

print('\n')
begin_time = time.time()
threads = []
for index in url_list:
    print(index)
    one_thread = threading.Thread(target=surf_net(index),args=(index,))
    threads.append(one_thread)
for j in threads:
    j.start()
for j in threads:
    j.join()
stop_time = time.time()
print(stop_time)