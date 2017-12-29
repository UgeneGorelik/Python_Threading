#example of using Q to share resources

#import Queue module
import queue
import threading


lock=threading.Lock()

count=0

#regular q
def append_t_queue(name):
    q.put(name)

#priority Queu
def append_t_Pqueue():
    global  count
    with lock:
     pq.put(count)
     count+=1


#init queue
q=queue.Queue()

#declare and start threads
t=threading.Thread(target=append_t_queue,args=("t1",))
t1=threading.Thread(target=append_t_queue,args=("t2",))

t.start()
t1.start()
t.join()
t1.join()

#print what Queu contians
while not q.empty():
    print(q.get())


#same just use priority Q
pq=queue.PriorityQueue()

t3=threading.Thread(target=append_t_Pqueue)
t4=threading.Thread(target=append_t_Pqueue)

t3.start()
t4.start()
t3.join()
t4.join()

while not pq.empty():
    print(pq.get())