import re
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

from JsSpider.login.chaojiying import Chaojiying_Client
import random
import requests

USERNAME =  '18737540525'
PASSWORD = 'hrx114526'

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
driver.get("https://passport.bilibili.com/login?from_spm_id=333.999.top_bar.login_window")
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="login-username"]').send_keys(USERNAME)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys(PASSWORD)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()
time.sleep(3)
def verify():
    code_pic = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/div/div/div[2]/div[1]/div/div[2]/img')
    img = code_pic.screenshot_as_png
    chaojiying = Chaojiying_Client('18737540525', 'hrx114526', '922995')
    dic = chaojiying.PostPic(img, 9004)
    verfity_code = dic['pic_str']
    # 输入信息
    print(verfity_code)
    point_list = verfity_code.split('|')
    new_list = []
    for point in point_list:
        xy = point.split(',')
        temp = [int(xy[0]), int(xy[1])]
        new_list.append(temp)
    print(new_list)
    for point in new_list:
        x = point[0]
        y = point[1]
        ActionChains(driver).move_to_element_with_offset(code_pic, x, y).click().perform()
        time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/div/div/div[3]/a/div').click()
    # content = driver.page_source
    # but = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/div/div/div[2]/div[2]').text
    # print('验证状态',content)
    # if '验证成功' in content:
    #     time.sleep(20)
    #     driver.close()
    # else:
    #     verify()
    #     print('验证失败，正在重新验证。。。。。。')
    time.sleep(20)
    driver.close()
if __name__ == '__main__':
    verify()



