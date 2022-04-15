from threading import Thread
from threading import Lock
import time 

class MyThread(Thread):
    def __init__(self, thread_id, thread_name, counter):
        Thread.__init__(self)
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.counter = counter
    
    
    def run(self):
        print("starting" +self.thread_name)
        threadLock.acquire()
        print_time(self.thread_name, self.counter, 3)
        threadLock.release()
    
def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print(thread_name, time.ctime(time.time()))
        counter -=1
    
threadLock = Lock()

threads = []

thread1 = MyThread(1, 'thread-1', 1)
thread2 = MyThread(2, 'thread-2', 2)
    
thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

print(thread1.daemon)

for t in threads:
    t.join()
print("exit main thread")