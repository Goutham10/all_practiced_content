import _thread
import time


def thread_test(name, wait):
    i = 0
    while i <= 3:
        time.sleep(wait)
        print("Running", name)
        i += 1

        print("finished execution")
    

if __name__ == "__main__":
    _thread.start_new_thread(thread_test,("First Thread", 1))

    