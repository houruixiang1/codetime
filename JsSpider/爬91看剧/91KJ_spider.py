import re
import requests
import os

# if not os.path.exists('./m3u8文件/'):
#     os.mkdir('./m3u8文件/')
#
# if not os.path.exists('./ts文件/'):
#     os.mkdir('./ts文件/')
#
# url="https://www.91kanju.com/vod-play/54812-1-1.html"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
# }
#
# resp = requests.get(url=url,headers=headers,verify=False)
# # print(resp.text)
# n = '哲仁王后'
# opt = re.compile("url: '(?P<url>.*?)',",re.S)
# m3u8_url = opt.search(resp.text).group('url')
# # print(m3u8_url)
# with open('./m3u8文件/'+f'{n}'+'.m3u8',mode='wb')as f:
#     resp1 = requests.get(url=m3u8_url,headers=headers,verify=False)
#     content =resp1.content
#     f.write(content)
# print("下载m3u8文件成功！")
# n=1
# with open('./m3u8文件/哲仁王后.m3u8',mode='r',encoding='utf-8')as f:
#     for line in f:
#         # line1 = line.split(f'#')[0]
#         line = line.strip()
#         # opt1 = re.compile(f',(?P<url>.*?)#',re.S)
#         # line = opt1.search(line).group('url')
#         # print(line)
#
#         if line.startswith('#'):
#             continue
#         # print(line)
#
#         resp2 = requests.get(line)
#         f = open('./ts文件/'+ str(n) +'.ts',mode='wb')
#         f.write(resp2.content)
#         f.close()
#         resp2.close()
#         n += 1
#         print(f"第{n}片段下载完成")
from imageio.plugins import ffmpeg

lst=[]
for i in range(1,153):
    x = f'{i}'+'.ts'
    # print(x)
    lst.append(x)
# print(lst)
s="+".join(lst)
print(s)
os.system(f"ffmpeg -i {s}.ts out.mp4")

# ffmpeg -i .\Video.avi -c copy -map 0 video.mp4
print("合并电影成功！")







