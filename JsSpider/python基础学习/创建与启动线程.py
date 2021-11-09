import threading
import time
def eat(n):
    print("eat(%s)"%n)
    time.sleep(1)
def dring(n):
    print("dring(%s)"%n)
    time.sleep(2)
q1 = threading.Thread(target=eat,args=(1,))
q2 = threading.Thread(target=dring,args=(2,))
q1.start()
q2.start()
# q1.join()
# q2.join()
print("...in the main...")