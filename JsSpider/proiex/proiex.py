import random
import subprocess as sp
from bs4 import BeautifulSoup
import requests
from lxml import etree
import re
class get_pro():
    def get_proxys(self,page = 1):
        target_url = 'https://www.kuaidaili.com/free/inha/%d' % page

        target_headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer':'https://www.kuaidaili.com/free',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'zh-CN,zh;q=0.8',
        }
        #get请求
        target_response = requests.get(url = target_url, headers = target_headers)
        #utf-8编码
        target_response.encoding = 'utf-8'
        #获取网页信息
        target_html = target_response.text
        # print(target_html)
        bs = BeautifulSoup(target_html,'html.parser')
        tbody = bs.find("tbody")
        html = etree.HTML(str(tbody))
        opts = html.xpath("//tbody/tr")
        # print(opts)
        proxys_list = []
        for opt in opts:
            ip = opt.xpath("./td[1]/text()")
            type = opt.xpath("./td[4]/text()")
            port = opt.xpath("./td[2]/text()")
            proxys_list.append(type[0].lower() + '#' + ip[0] + '#' + port[0])
        return proxys_list
        # print(tbody)
        # ip_list = re.finditer('data-title="IP">(.*?)</td>',str(tbody),re.S)
        # for item in ip_list:
        #     print(item.group(1))
        # port_list = re.finditer('data-title="PORT">(.*?)</td>',str(tbody),re.S)
        # for item in port_list:
        #     print(item.group(1))
        # type_list = re.finditer('data-title="类型">(.*?)</td>', str(tbody), re.S)
        # for item in type_list:
        #     print(item.group(1))
    def check_ip(self,ip, lose_time, waste_time):
        #命令 -n 要发送的回显请求数 -w 等待每次回复的超时时间(毫秒)
        cmd = "ping -n 3 -w 3 %s"
        #执行命令
        p = sp.Popen(cmd % ip, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, shell=True, encoding = "gbk")
        #获得返回结果并解码
        # print(p.stdout.read())
        out = p.stdout.read()
        #丢包数
        lose_time = lose_time.findall(out)
        #当匹配到丢失包信息失败,默认为三次请求全部丢包,丢包数lose赋值为3
        if len(lose_time) == 0:
            lose = 3
        else:
            lose = int(lose_time[0])
        #如果丢包数目大于2个,则认为连接超时,返回平均耗时1000ms
        if lose > 2:
            #返回False
            return 1000
        #如果丢包数目小于等于2个,获取平均耗时的时间
        else:
            #平均时间
            average = waste_time.findall(out)
            #当匹配耗时时间信息失败,默认三次请求严重超时,返回平均好使1000ms
            if len(average) == 0:
                return 1000
            else:
                #
                average_time = int(average[0])
                #返回平均耗时
                return average_time

    def initpattern(self):
        #匹配丢包数
        lose_time = re.compile(u"丢失 = (\d+)", re.IGNORECASE)
        #匹配平均时间
        waste_time = re.compile(u"平均 = (\d+)ms", re.IGNORECASE)
        return lose_time, waste_time

    # if __name__ == '__main__':
    def main(self):
        #初始化正则表达式
        lose_time, waste_time = self.initpattern()
        #获取IP代理
        proxys_list = self.get_proxys(1)

        #如果平均时间超过200ms重新选取ip
        while True:
            #从100个IP中随机选取一个IP作为代理进行访问
            proxy = random.choice(proxys_list)
            split_proxy = proxy.split('#')
            #获取IP
            ip = split_proxy[1]
            #检查ip
            average_time = self.check_ip(ip, lose_time, waste_time)
            if average_time > 200:
                #去掉不能使用的IP
                proxys_list.remove(proxy)
                print("ip连接超时, 重新获取中!")
            if average_time < 200:
                break

        #去掉已经使用的IP
        proxys_list.remove(proxy)
        proxy_dict = {split_proxy[0]:split_proxy[1] + ':' + split_proxy[2]}
        # print("使用代理:", proxy_dict)
        return proxy_dict
if __name__ == '__main__':
    task = get_pro()
    print(task.main())


