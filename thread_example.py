import time
import threading


def calc_sq(numbers):
    print("square")
    for x in numbers:
        time.sleep(0.2)
        print("sq " +str(x*x))

def calc_cu(numbers):
    print("cube")
    for x in numbers:
        time.sleep(0.2)
        print("cube"+ str(x*x*x))



arr =[1,2,3]

t1=threading.Thread(target=calc_sq,args=(arr,))
t2=threading.Thread(target=calc_cu,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

