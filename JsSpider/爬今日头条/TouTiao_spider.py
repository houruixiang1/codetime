import requests


url=("https://so.toutiao.com/search?keyword={}&pd=information&source"
     "=search_subtab_switch&dvpf=pc&aid=4916&page_num=0").format('国足')
# print(url)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Cookie':'_S_DPR=1.5; _S_IPAD=0; MONITOR_WEB_ID=7009566273484097031; ttwid=1%7CyI46daTxZyFZxhEo-FBHOmY1mXhXW5Ymh8_rquQuEMc%7C1632447737%7C69a19b4473d5dd8a0e263fe3cca7479f771a62e4c2fd0b833b99a377e222c0b2; _S_WIN_WH=1217_150'}
resp = requests.get(url=url,headers=headers)
print(resp.text)