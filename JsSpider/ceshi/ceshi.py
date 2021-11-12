print("输入1，代表执行")
print("输入2，代表退出")

while(1):
    k = input("请输入你要选择的号数(仅限1和2)：")
    if 50<=int(k)<=200:
        print('输入正确！')
        url = 'http://www.sdvhasoivhdaoshdv{}'.format(int(k))
        print(url)
        break
    # elif int(k)==2:
    #     print(2+2)
    else:
        print('输入有误！,请重新输入')
        continue

