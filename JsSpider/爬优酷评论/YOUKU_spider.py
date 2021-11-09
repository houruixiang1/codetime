import requests

url="https://acs.youku.com/h5/mtop.youku.ycp.comment.mainpage.get/1.0/?jsv=2.6.1&appKey=24679788&t=1632316064848&sign=463a9b75f07e9b98c1cc05ca6ebaa4fc&api=mtop.youku.ycp.comment.mainpage.get&type=originaljson&v=1.0&ecode=1&dataType=json&data=%7B%22app%22%3A%22100-DDwODVkv%22%2C%22time%22%3A1632316064834%2C%22objectCode%22%3A%22XNTE1MTgxMDE2NA%3D%3D%22%2C%22objectType%22%3A1%2C%22sign%22%3A%224253a1dfaae5f8eee8669b792a5e3191%22%7D"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
,   "Cookie": 'cna=sPd1GFIWLRYCAXjCnuLwT79o; _m_h5_tk=67e60807599c45f1f162e5af21870c78_1632319547861; _m_h5_tk_enc=1d1a7ce4192d9418ca971a14821d2756; __ysuid=1632315771729pND; __ayft=1632315771730; __ayscnt=1; __aysid=1632315771730Lso; P_ck_ctl=52C7E7FDA65108474654E05F90F6B4BE; UM_distinctid=17c0d9a12d8787-065277a6f0a14f-a7d173c-e1000-17c0d9a12d9e0f; xlly_s=1; redMarkRead=1; __arycid=dh-3-00; __arcms=dh-3-00; modalFrequency={"UUID":"2"}; __ayvstp=12; __aysvstp=12; l=eBIDTZnrgR8SmS0ZBO5wKurza77tCIOf1sPzaNbMiInca6LFTCrycNCLsoMD7dtjgt5vQetrd8LeqRHv52ULRFkDBeYINV_Mfv96Re1..; tfstk=c-p5BymQmz47_EcUU3i4839UFxWhawlfDb_2VBwX94iT_YtPks4LQNNCqB4bH1If.; isg=BKWlkzNNKO852EyzPruPofdMtGHf4ll0w9_gHKeLBFxgvsYwbzAGROkfSCLIvnEs; __arpvid=1632316062751CKSDkV-1632316062819; __aypstp=8; __ayspstp=8'
}
resp = requests.get(url=url,headers=headers)
print(resp.text)