import requests
import asyncio
import aiohttp
import aiofiles
import json
import os

if not os.path.exists('./西游记/'):
    os.mkdir('./西游记/')
# title_url='https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}'
# content_url = 'https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|11348571","need_bookinfo":1}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
}
async def aiodownload(b_id,cid,title):
    data={
        "book_id":b_id,
        "cid":f"{b_id}|{cid}",
        "need_bookinfo":1
    }
    data = json.dumps(data)
    content_url = f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url=content_url,headers=headers) as resp:
            dic = await resp.json()
            # print(dic)
            async with aiofiles.open("./西游记/"+title,mode='w',encoding='utf-8')as f:
                await f.write(dic['data']['novel']['content'])

async def get_title(url):
    resp = requests.get(url=url,headers=headers)
    dic = resp.json()
    tasks=[]
    for d in dic['data']['novel']['items']:
        title = d['title']
        cid = d['cid']
        tasks.append(aiodownload(b_id,cid,title))
    await asyncio.wait(tasks)

def get_content():
    pass

if __name__ == '__main__':
    b_id = '4306063500'
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}'
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_title(url))

