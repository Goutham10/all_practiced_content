from threading import Thread
import time
import queue

class MyThread(Thread):

    def __init__(self, thread_name, thread_id):
        Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_id = thread_id

    def run(self):
        print(self.thread_name, self.thread_id)

nameList = ["One", "Two", "Three", "Four", "Five"]
    
a = MyThread('thread_1', 1)
a.start()

workqueue = queue.Queue()

for word in nameList:
    workqueue.put(word)

while not workqueue.empty():
    print(workqueue.get())

