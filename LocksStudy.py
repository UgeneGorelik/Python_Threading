#basic example on Thread locks

import threading


#define Lock
lock=threading.Lock()
x=100

#function to be threaded
def add_1():
    global x

    #use lock so that only current thread can acsses resource
    with lock:
        x+=1


def sub_1():
    global x
# use lock so that only current thread can acsses resource
    with lock:
        x -= 1

def mul_2():
    global x
#basically what with lock does is acqires lock and releases lock so its bassicaly the same
#that with lock
    lock.acquire()
    x *= 2
    lock.release()


t=threading.Thread(target=add_1())
t2=threading.Thread(target=sub_1())
t3=threading.Thread(target=mul_2())

t.start()
t2.start()
t3.start()

t.join()
t2.join()
t3.join()
print(x)