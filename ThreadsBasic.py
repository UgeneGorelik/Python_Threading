#basic threadinf Example

import threading
import time





def ThreadNo(n,name):
    print("Hi i am "+ name +" i am tired will sleep for a while ")
    time.sleep(n)
    print("Hi i am " + name + " its time to wake Up ")

#initiate tread
t=threading.Thread(target=ThreadNo,name='First Thread Example',args=(5,"Thread1"))

#start tread
t.start()

print("meanwhile Thread1 is asleep i am going out to play")

#main program wait for thread to finish
t.join()

print("okies Thread1 is finished ")


t_list = []

start_time=time.time()

#create list of threads
for i in range(3):
    x=threading.Thread(target = ThreadNo,name="Thread"+str(i),args=(5,"Thead"+str(i)) )
    t_list.append(x)
    x.start()

#main process waits untill threasd are finished
for  t in t_list:
    t.join()

print("all threads done")
end_time=time.time()

#take time  of the all threads ran in list
print("time all threads ran:" +str(abs(end_time-start_time)))