import codecs
import json
import re

import requests

import csv

# with open('爬虫职位.csv',mode='a',encoding='utf-8',newline='')as f:
#     csv_write = csv.DictWriter(f,fieldnames=['name', 'providesalary_text', 'company_name', 'companytype_text', 'workarea_text', 'attribute_text', 'companysize_text', 'companyind_text', 'jobwelf', 'updatedate'])
#     csv_write.writeheader()

f = codecs.open('爬虫工程师岗位薪资.csv','a','utf-8')
writer = csv.writer(f)
writer.writerow(['name', 'providesalary_text', 'company_name', 'companytype_text', 'workarea_text', 'companysize_text', 'companyind_text', 'jobwelf', 'updatedate'])
def parse(url):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    resp = requests.get(url=url,headers=headers).text
    # print(resp)
    data = re.search('window.__SEARCH_RESULT__ = (.*?)</script>',resp,re.S).group(1).strip()
    # print(data)
    json_data = json.loads(data)
    for one_data in json_data['engine_jds']:
        name = one_data['job_name']
        providesalary_text = one_data['providesalary_text']
        company_name = one_data['company_name']
        companytype_text = one_data['companytype_text']
        workarea_text = one_data['workarea_text']
        companysize_text = one_data['companysize_text']
        companyind_text = one_data['companyind_text']
        jobwelf = one_data['jobwelf']
        updatedate = one_data['updatedate']
        writer.writerow([name + "", providesalary_text + "", company_name + "", companytype_text + "",
                         workarea_text + "",companysize_text + "",companyind_text + "",jobwelf + "",updatedate + ""])

if __name__ == '__main__':
    for i in range(1,33):
        url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E7%2588%25AC%25E8%2599%25AB,2,{}.html?'.format(i)
        parse(url)
        print("正在爬取{}页".format(i))