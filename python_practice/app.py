from threading import Thread
import time

exitflag = 0

class Data(Thread):
    def __init__(self, thread_id, thread_name, counter):
        super().__init__()
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.counter = counter
        print("in constructor")

    def run(self):
        print("start")
        print_time(self.thread_id, self.thread_name, self.counter)
        # time.sleep(1)
        print("end")

def print_time(thread_id, thread_name, delay):
    while delay:
        if exitflag:
            thread_name.exit()
        time.sleep(delay)
        print(thread_name, thread_id, time.time())
        delay -=1 

a = Data(101, "thread-1", 1)
b = Data(102, "thread-2", 2)
a.start()
b.start()

a.join()
b.join()
