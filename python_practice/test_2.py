from threading import Thread
import time


def sleeper(n, name):
    print(name)
    time.sleep(n)
    print(name)
    print("end")

t = Thread(target= sleeper, name="thread-1", args= (5, "goutham"))
t.start()
# t.join()
print("asjbjsa")