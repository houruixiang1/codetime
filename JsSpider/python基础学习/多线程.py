from threading import Thread

def func(name):
    for i in range(1000):
        print(name,i)

if __name__ == '__main__':
    t=Thread(target=func,args=("黄飞鸿",))
    t.start()
    t1 = Thread(target=func, args=("李连杰",))
    t1.start()
    # t.join()
    for i in range(1000):
        print("陈真",i)