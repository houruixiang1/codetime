import requests
import re
# name = input("请输入商品名称： ")
url= 'https://h5api.m.taobao.com/h5/mtop.alimama.union.xt.en.api.entry/1.0/?jsv=2.5.1&appKey=12574478&t=1637737940907&sign=6cadb1e05c63ad646de42f3ccbf92163&api=mtop.alimama.union.xt.en.api.entry&v=1.0&AntiCreep=true&timeout=20000&AntiFlood=true&type=jsonp&dataType=jsonp&callback=mtopjsonp2&data=%7B%22pNum%22%3A0%2C%22pSize%22%3A%2260%22%2C%22refpid%22%3A%22mm_26632258_3504122_32538762%22%2C%22variableMap%22%3A%22%7B%5C%22q%5C%22%3A%5C%22%E6%B2%99%E5%8F%91%5C%22%2C%5C%22navigator%5C%22%3Afalse%2C%5C%22clk1%5C%22%3A%5C%22eaf8cee15b76ccafca5144002beb192e%5C%22%2C%5C%22union_lens%5C%22%3A%5C%22recoveryid%3A201_11.20.207.176_40621474_1637735464160%3Bprepvid%3A201_11.92.48.8_40583555_1637737814141%5C%22%2C%5C%22recoveryId%5C%22%3A%5C%22201_11.170.86.128_40587606_1637737941394%5C%22%7D%22%2C%22qieId%22%3A%2236308%22%2C%22spm%22%3A%22a2e0b.20350158.31919782%22%2C%22app_pvid%22%3A%22201_11.170.86.128_40587606_1637737941394%22%2C%22ctm%22%3A%22spm-url%3Aa2e0b.20350158.search.1%3Bpage_url%3Ahttps%253A%252F%252Fuland.taobao.com%252Fsem%252Ftbsearch%253Frefpid%253Dmm_26632258_3504122_32538762%2526keyword%253D%2525E6%2525B2%252599%2525E5%25258F%252591%2526clk1%253Deaf8cee15b76ccafca5144002beb192e%2526upsId%253Deaf8cee15b76ccafca5144002beb192e%2526spm%253Da2e0b.20350158.search.1%2526pid%253Dmm_26632258_3504122_32538762%2526union_lens%253Drecoveryid%25253A201_11.20.207.176_40621474_1637735464160%25253Bprepvid%25253A201_11.92.48.8_40583555_1637737814141%22%7D'
headers = {
                                                                                                            # %22variableMap%22%3A%22%7B%5C%22q%5C%22%3A%5C%22%E6%B2%99%E5%8F%91%5C%22%2C
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 't=f3a1f583e5ce55a90423fb15cfe72246; sgcookie=E100huyQ%2FypzUED%2FicX%2Bs4M%2F3pz4oCAz0OtHlgYdbabUleFDdjlGHd%2BACeFj6hNPYzvG%2FmOBNf0javf7fF08iP%2F%2Bnp7p%2FFcqq7Un%2FpQim44ii%2Bs%3D; thw=cn; mt=ci=0_0; tracknick=; cna=E0voGTIo93kCAbcOHjGJdraK; _m_h5_tk=94cd776b42a604230f77a354c0fed854_1637742664640; _m_h5_tk_enc=dd859e52ac095222f9c54d7e082a10fc; xlly_s=1; _samesite_flag_=true; cookie2=124d8c1df9cde2f90c7b9c1935c95ee8; _tb_token_=efde43817e3bb; isg=BICAfzyj9d5TCYkxLbAHjDFDUQ5SCWTTRoriiPoSIxs1dSGfoh5LYz4Ejd21RRyr; l=eB_1LKnlgwBLRapJBO5ahurza77O5QOb8sPzaNbMiInca6_lOeHdiNCddPe65dtjgtfvcetrRRzQkRhvo6zdNxDDBecuBKWtMc96-; tfstk=co-FB3arfDnFEvjSkMsrR_LOan9da2vHElWf-e53irjU4y_dgsVzwOftDOW7Q7bh.',
    'referer': 'https://uland.taobao.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
resp = requests.get(url=url,headers=headers)
print(resp.text)