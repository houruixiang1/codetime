import requests


url="https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
# 1.headers中加cookie
# headers={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
#   , 'Cookie':'GUID=6abb285f-7390-4df1-8d5e-0206ba682592; BAIDU_SSP_lcr=https://www.baidu.com/link?url=Hyt4HL8vQRJ403TEcEE6Oety2GEsFvAvjyO2rrGYrYS&wd=&eqid=d105d85a0001d44500000003614a96c6; sajssdk_2015_cross_new_user=1; Hm_lvt_9793f42b498361373512340937deb2a0=1632278227; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F07%252F67%252F97%252F80909767.jpg-88x88%253Fv%253D1632278487443%26id%3D80909767%26nickname%3D%25E6%2597%25B6%25E5%2585%2589%25E5%25B0%2591%25E5%25B9%25B4_%25E7%25A5%25A5%26e%3D1647830487%26s%3D1c158530dc77b914; c_channel=0; c_csc=web; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2280909767%22%2C%22%24device_id%22%3A%2217c0b5d27e0be-087196ca7c9571-a7d173c-921600-17c0b5d27e1a67%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%226abb285f-7390-4df1-8d5e-0206ba682592%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1632278549'
# }
#
#
# resp = requests.get(url=url,headers=headers)
# print(resp.json())


# 2.session

session = requests.session()
urls = 'https://passport.17k.com/ck/user/login'
data={
    'loginName': '18737540525',
    'password': 'hrx114526'
}
response = session.post(url=urls,data=data)
# print(response.text)
resp = session.get(url=url)
print(resp.json())


