# import multiprocessing

# def cal_sq(numbers, result):
#     for idx, n in enumerate(numbers):
#         result[idx] = n * n
    
# if __name__ == "__main__":
#     numbers = [2, 3, 5]
#     result = multiprocessing.Array('i', len(numbers))
#     p = multiprocessing.Process(target=cal_sq, args=(numbers, result))

#     p.start()
#     p.join()

#     print(result[:])

    
####################################################
import multiprocessing

def cal_cube(numbers, q):
    for n in numbers:
        q.put(n ** 3)

if __name__ == "__main__":
    numbers = [2,3,4]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=cal_cube, args=(numbers,q))

    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())