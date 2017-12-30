#simple example on Pools

#import Lib
from  multiprocessing import  Pool

#define function to run on parralel CPUS
def foo(n):
    return  n*n

#madatory for Multiprocessing to be ran from main

if __name__=="__main__":

    arr=[1,2,3]

#declare pool
    p=Pool()
#Map function to pool
    result=p.map(foo,arr)
    print(result)
