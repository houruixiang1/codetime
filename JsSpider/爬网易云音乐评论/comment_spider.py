import requests


url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
}





data={
    "params":"x",
    "encSecKey":"y"
}
requests.get(url=url,headers=headers,data=data)