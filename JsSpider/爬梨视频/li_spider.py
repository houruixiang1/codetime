#  真正的url：‘https://video.pearvideo.com/mp4/third/20210921/cont-1742182-10054243-145024-hd.mp4’
#  假的俩：   ‘https://video.pearvideo.com/mp4/third/20210921/1632281675518-10054243-145024-hd.mp4’
import os

import requests

url='https://www.pearvideo.com/video_1742182'
contId = url.split('_')[-1]
# print(contId)
if not os.path.exists('./liVideo/'):
    os.mkdir('./liVideo/')


url1 ='https://www.pearvideo.com/videoStatus.jsp?contId=1742182&mrd=0.7438790624827694'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Referer":"https://www.pearvideo.com/video_1742182"
}

resp = requests.get(url=url1,headers=headers)
# print(resp.json())
srcUrl = resp.json()['videoInfo']['videos']['srcUrl']
systemTime = resp.json()['systemTime']
srcUrl = srcUrl.replace(systemTime,f'cont-{contId}')
# print(srcUrl)

with open('./liVideo/'+contId+'.mp4',mode='wb') as f:
    f.write(requests.get(srcUrl).content)
print("视频下载成功！")
