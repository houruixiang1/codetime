import hashlib
import random
import time

import requests
from PIL import Image

session = requests.session()
ver_code_url = 'https://login.xinshangmeng.com/login/users/forlogin/img'
headers = {
    'Referer': 'http://www.xinshangmeng.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

def encry_pwd(pwd):
    pwd = pwd + '{1#2$3%4(5)6@7!poeeww$3%4(5)djjkkldss}'
    md5 = hashlib.md5()
    md5.update(pwd.encode('UTF-8'))
    password = md5.hexdigest()
    return password

def get_code():
    response = session.get(url=ver_code_url, headers=headers)
    # print(response)
    with open('C:\CodeTime\img\新商盟login_code.png', 'wb') as f:
        f.write(response.content)
    image = Image.open('C:\CodeTime\img\新商盟login_code.png')
    image.show()
    code = input('请输入验证码: ')
    return code

def login(username, encrypted_password, code):
    # timestamp = str(round(time.time() * 1000))
    # jsonp = ''
    # for _ in range(20):
    #     jsonp += str(random.randint(0, 9))
    # jsonp = 'jQuery' + jsonp + '_' + timestamp
    params = {
        # 'jsonp': jsonp,
        'protocol': 'http:',
        'loginIndex': 'http://xinshangmeng.com/xsm2/?Version=2021111300',
        'j_mmrm': username,
        'j_mcmm': encrypted_password,
        'j_valcode': code,
        # '_': timestamp
    }
    response = session.get(url='http://login.xinshangmeng.com/login/users/dologin/dfaup?', params=params, headers=headers)
    response.encoding = 'utf-8'
    print(response.text)

if __name__ == '__main__':
    code = get_code()
    pwd1 = encry_pwd('123456')
    pwd2 = encry_pwd(pwd1)
    print(pwd2)
    login('18737540525',pwd2,code)
