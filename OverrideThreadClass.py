import threading
import time

#Here we copied the Thread Class from the original code
class MyThread(threading.Thread):
    def run(self):
#here we added a print by ourselfs
        print("Gotcha i am Subclass")
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs
        print('{} has finished!'.format(self.getName()))


#same stuff function to be ran threaded
def ThreadNo(*args):
    print("Hi i am "+ args[0] +" i am tired will sleep for a while ")
    time.sleep(1)
    print("Hi i am " + args[0] + " its time to wake Up ")

#defining and starting thread
t=MyThread(target=ThreadNo,name='First Thread Example',args=("T"))

t.start()