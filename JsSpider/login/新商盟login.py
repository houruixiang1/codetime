import hashlib
def encry_pwd(pwd):
    pwd = pwd + '{1#2$3%4(5)6@7!poeeww$3%4(5)djjkkldss}'
    md5 = hashlib.md5()
    md5.update(pwd.encode('UTF-8'))
    password = md5.hexdigest()
    return password
pwd1 = encry_pwd('123456')
pwd2 = encry_pwd(pwd1)
print(pwd2)