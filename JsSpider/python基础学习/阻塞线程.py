import threading
from time import ctime,sleep
import time

def music(par):
    for i in range(2):
        print("Begin listening to %s.%s" %(par,ctime()))
        sleep(2)
        print("end listening %s"%ctime())

def movie(par):
    for i in range(2):
        print("Begin watching to %s.%s" %(par,ctime()))
        sleep(3)
        print("end watching %s"%ctime())

threads = []
x1 = threading.Thread(target = music,args=('最炫民族风',))
threads.append(x1)
x2 = threading.Thread(target = movie,args=('泰坦尼克号',))
threads.append(x2)

if __name__ == '__main__':
    for x in threads:
        x.start()
        x.join()
    print("All is over %s" %ctime())