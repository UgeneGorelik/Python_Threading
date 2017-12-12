import  multiprocessing
import time

def calc_sq(numbers):
    print("square")
    for x in numbers:

        print("sq " +str(x*x))

def calc_cu(numbers):
    print("cube")
    for x in numbers:

        print("cube"+ str(x*x*x))

arr=[1,2,3]
p1 = multiprocessing.Process(target=calc_sq,args=(arr,))
