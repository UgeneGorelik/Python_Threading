#!/usr/bin/env python
#-----------------------------------------------------------------------------
# This example will show how to use multiprocessing
# it will run 2 functions in parallel as a process
#-----------------------------------------------------------------------------


import multiprocessing


#Function to calculate Square

def calc_sq(numbers):
    print("square")
    for x in numbers:

        print("sq " +str(x*x))

#Function to calculate Cube

def calc_cu(numbers):
    print("cube")
    for x in numbers:

        print("cube"+ str(x*x*x))


if __name__ == '__main__':

    # initialising an array
    arr=[1,2,3]

    #defining a process to run as multiprocess

    p1 = multiprocessing.Process(target=calc_sq,args=(arr,))
    p2 = multiprocessing.Process(target=calc_cu, args=(arr,))

    #Starting the process

    p1.start()
    p2.start()
