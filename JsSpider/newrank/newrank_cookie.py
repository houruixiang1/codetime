import time

from selenium import webdriver
from selenium.webdriver import ActionChains

url = 'https://newrank.cn/user/login'


def login():
    user_pwd = {
        '18737540525': 'Hrx1537',
        # 'c3y65sddsfg3303@foxmail.com': '8102mmEasub',
        # '5reqsds629@foxmail.com': 'lishi180828',
    }
    for k, v in user_pwd.items():
        # n_str = 'weibo_' + k
        # n_str = n_str[0:25]
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
        cookie_str = ''
        cookies = driver.get_cookies()
        for cookie in cookies:
            cookie_s = cookie['name'] + '=' + cookie['value'] + '; '
            cookie_str += cookie_s
        cookie_str = cookie_str[:-2]
        print(cookie_str)

if __name__ == '__main__':
    login()