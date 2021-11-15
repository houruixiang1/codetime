import csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path = 'C:\Program Files\Python37\chromedriver.exe')
# driver = webdriver.Chrome()

driver.get('https://www.gia.edu/report-check?reportno=9D3E6AE076A3F45520301F9DBFFA4C6C&qr=true')
resp = driver.page_source
# print(resp)

file =open('C:\CodeTime\JsSpider\ceshi\ceshi2.csv',mode='a',encoding='utf-8',newline='')
csv_write = csv.DictWriter(file,fieldnames=['key','value'])
csv_write.writeheader()
html = etree.HTML(resp)
text = [1,2,3,4,5,7]
for i in text:
    opt = '//div[@class="tab-content current"]/table[{}]/tbody/tr'.format(i)
    lists1 = html.xpath(opt)
    for list in lists1:
        xx = list.xpath('./td[1]/div/span/div/div/text()')
        xx = str(xx).replace('[','').replace(']','').replace("'","").replace(' ','').strip()
        yy = list.xpath('./td[2]/strong/text()')
        yy = str(yy).replace('[', '').replace(']', '').replace("'", "").replace(' ', '').strip()
        data_dict = {'key': xx, 'value': yy}
        csv_write.writerow(data_dict)
