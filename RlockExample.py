import queue
import threading
import time
from threading import Lock

g =0

#reentrant Lock can set how many times we lock this resource and it can be unlocked only from the current thread
#it solves reetntrancy problem(like a program can be interrupted and started over again

lock=threading.RLock()

def add_one():
    global g
    lock.acquire()
    g+=1
    lock.acquire()
    g += 1
    lock.release()

def add_two():
    global g
    lock.acquire()
    g+=2
    lock.release()

if __name__=="__main__" :

    t1=threading.Thread(target=add_one())
    t2=threading.Thread(target=add_two())

    t1.start()
    t2.start()

    print(g)

