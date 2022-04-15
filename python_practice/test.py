# from threading import *
# import time



# class A(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello")
#             time.sleep(1)


# class B(Thread):
#     def run(self):
#         for i in range(5):
#             print('hi')
#             time.sleep(1)

# t1 = A()
# t2 = B()

# t1.start()
# time.sleep(0.2)
# t2.start()

# t1.join()
# t2.join()
# print("bye")


from threading import *
import time

def cal_square(n):
    for i in n:
        time.sleep(0.2)
        print('square : ', i * i)
def cal_cube(n):
    for i in n:
        time.sleep(0.2)
        print('cube : ', i * i * i)

arr = [2,3,8,9]

t = time.time()
t1 = Thread(target=cal_square, args=(arr,))
t2 = Thread(target=cal_cube, args=(arr,))

t1.start()
t2.start()
t1.join()
t2.join()
