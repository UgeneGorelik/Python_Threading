import queue
import threading
import time

#example of Events (the raise flag as when thread can proceed or he should wait for flag)

#init event
event=threading.Event()

#function that raises flag for
def raise_flag():
    time.sleep(2)
#set flag to up
    event.set()
    print('Ahoy black flag is up pirates can Pillage')
    time.sleep(0.5)
#set flag to down
    event.clear()


#function that waits for flaf
def pirates_pillage():
#wait for flag to be up
    event.wait()
#run while flag is up
    while event.is_set():
        time.sleep(0.3)
        print("Pirates are pillaging")
    print("British are here ,hide the flag")


t=threading.Thread(target=raise_flag)
t1=threading.Thread(target=pirates_pillage)

t.start()
t1.start()
t.join()
t1.join()
