import datetime
import os
import sys
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

url = 'https://newrank.cn/user/login'

# par_dir = os.path.dirname(os.path.abspath(__file__)) + '/../..'
# os.chdir(par_dir)
# sys.path.append(par_dir)
#
# import pymysql
# from service import utils
#
# config = utils.read_config('C:\clip-genspider\config\db.yaml')  # 实例化
# if not config:
#     config = utils.read_config('../../../config/db.yaml')
#
# """
# Config是一些数据库的配置文件,通过调用我们写的readConfig来获取配置文件中对应值
# """
# host = config['databases']['mysql'].get('host')
# port = int(config['databases']['mysql'].get('port'))
# user = config['databases']['mysql'].get('user')
# passwd = config['databases']['mysql'].get('passwd')
# database = config['databases']['mysql'].get('db')
# dbchar = config['databases']['mysql'].get('charset')
#
# conn = pymysql.connect(host=host, port=port, db=database, user=user, password=passwd, charset=dbchar)

def login():
    user_pwd = {
        # '18737540525': 'Hrx1537',
        # '18339695822': 'yk123456',
        # '18321136376': '123456',
        # '15959110209': '123456789',
        # '18620346847': '18620346847',
        # 'guolan@staff.easub.com': '123456789',
        # '1093371528@qq.com': '123456789',
        # '13715012905': '123456789',
        # '18682464779': '123456789',
        # '15918559572': '123456789',   # 此账号不可用(账号或密码错误)
        # '851018790@qq.com': '123456789',
        # '1481746137@qq.com': '123456789',
        # '646124200@qq.com': '123456789',
        # '13662224763': '123456789',
        # '13129772843': '123456789',    # 此账号不可用(未注册)
        # 'duyuxiang@staff.easub.com': '123456789',
        # 'wangxuezhu@staff.easub.com': '123456789',
        # '13255948569': '123456789',
        # 'duyuxiang@staff.easub.com': '123456789',
        # 'wangxuezhu@staff.easub.com': '123456789',
        # '13255948569': '123456789',
        # '18576641238': '123456789',
        # '15399902468': '123456789',
        # '18682310095': '123456789',
        # 'chenqiang@staff.easub.com': '123456789',
        # 'argus_don@163.com': '123456789',
        # '572407910@qq.com': '123456789',
        '13590285692': '123456789',
    }
    create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for k, v in user_pwd.items():
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36')
        options.add_argument('--no-sandbox')
        options.add_argument('window-size=1920x3000')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-blink-features=AutomationControlled')

        driver = webdriver.Chrome(options=options)
        # print(k, v)
        driver.get(url)
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[1]/div[3]/span[1]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]/input').send_keys(k)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[2]/span/input').send_keys(v)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[4]/button').click()
        time.sleep(2)
        btn = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
        ActionChains(driver).drag_and_drop_by_offset(btn,300,0).perform()
        time.sleep(10)
        driver.execute_script("window.open('https://xd.newrank.cn/tiktok/detailV2/overview/7BE3911B8290E5078BE8B8363DF4557B')")
        # newrank_cookie = driver.get_cookies()
        # print(newrank_cookie)
        time.sleep(5)
        dy_cookie_str = ''
        cookies = driver.get_cookies()
        for cookie in cookies:
            cookie_s = cookie['name'] + '=' + cookie['value'] + '; '
            dy_cookie_str += cookie_s
        dy_cookie_str = dy_cookie_str[:-2]

        driver.execute_script(
            "window.open('https://xk.newrank.cn/data/d/account/trend/1096637401')")
        time.sleep(5)
        ks_cookie_str = ''
        cookies = driver.get_cookies()
        for cookie in cookies:
            cookie_s = cookie['name'] + '=' + cookie['value'] + '; '
            ks_cookie_str += cookie_s
        ks_cookie_str = ks_cookie_str[:-2]

        print('xxx', k, dy_cookie_str, ks_cookie_str)
        # if 'token' in str(dy_cookie_str):
        #     save(k, dy_cookie_str, ks_cookie_str, create_time)
        #     print('xxx',k, dy_cookie_str, ks_cookie_str)
        # else:
        #     print('此账号不可用', k)
        # print('xxx', k, dy_cookie_str, ks_cookie_str)
        driver.quit()

# def save(k, dy_cookie_str, ks_cookie_str, create_time):
#     # sql = '''
#     #     update newrank_cookie set cookies = '%s' where site = '%s' and isvip = 0
#     #     ''' % (cookie_str, n_str)
#     sql = "insert into newrank_cookie (iphone, cookies, ks_cookies, created_at) values ('%s','%s','%s','%s');" % (
#         k, dy_cookie_str, ks_cookie_str, create_time)
#     print(sql)
#
#     with conn.cursor() as cur:
#         cur.execute(sql)
#         conn.commit()
#         # print('插入成功')
#     return '插入成功'

if __name__ == '__main__':
    login()