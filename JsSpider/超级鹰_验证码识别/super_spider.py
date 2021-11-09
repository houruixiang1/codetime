import time
from chaojiying import Chaojiying_Client

from selenium.webdriver import Chrome

web = Chrome()

web.get("http://www.chaojiying.com/user/login/")
# time.sleep(10)
# 处理验证码
img = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('18737540525', 'hrx114526', '922995')
dic = chaojiying.PostPic(img, 1902)
verfity_code = dic['pic_str']
# 输入信息
print(verfity_code)
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('18737540525')
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('hrx114526')
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verfity_code)
time.sleep(10)
# 点击登录
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()
time.sleep(20)
web.close()