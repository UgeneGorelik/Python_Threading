#!/usr/bin/env python
#-----------------------------------------------------------------------------
# This example will show how to use threading
# it will run 2 functions in parallel as a a thread
#-----------------------------------------------------------------------------



import time
import threading

#Function to calculate Square

def calc_sq(numbers):
    print("square")
    for x in numbers:
        time.sleep(0.2)
        print("sq " +str(x*x))

#Function to calculate Cube

def calc_cu(numbers):
    print("cube")
    for x in numbers:
        time.sleep(0.2)
        print("cube"+ str(x*x*x))


# initialising an array
arr =[1,2,3]

# defining a process to run as multiprocess

t1=threading.Thread(target=calc_sq,args=(arr,))
t2=threading.Thread(target=calc_cu,args=(arr,))

# Starting the process

t1.start()
t2.start()

#waiting to thread to finis

t1.join()
t2.join()

