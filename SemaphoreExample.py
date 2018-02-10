from threading import BoundedSemaphore,Thread
import time,random

max_items =5


#semaphor gives us ability to choose the amount of times we can time the lock
#The counter is decremented when the semaphore is acquired,
# and incremented when the semaphore is released
#. If the counter reaches zero when acquired, the acquiring thread will block.
# When the semaphore is incremented again, one of the blocking threads  will run.

#declaring semaphpre that can contain 5 items
#means it gets full when its number is 5 and then we can reduce items

sem=BoundedSemaphore(max_items)

def producer(n):
    for x in range(n):
        time.sleep(random.randrange(2, 5))
        try:
            #release one from smaphore(
            sem.release()
            print("produced")
        except ValueError:
            print("full so so skipping")

def consumer(n):
    for x in range (n):
        time.sleep(random.randrange(2, 5))
        #check if we can use the semaphore
        if sem.acquire():
            print("consuming")
        else:
            print("empty so skipping")



threads = []
nloops = random.randrange(3, 6)
print("Starting with %s items." % max_items)
threads.append(Thread(target=producer, args=(nloops,)))
threads.append(Thread(target=consumer, args=(random.randrange(nloops, nloops + max_items + 2),)))
for thread in threads:  # Starts all the threads.
    thread.start()
for thread in threads:  # Waits for threads to complete before moving on with the main script.
    thread.join()
print("All done.")

