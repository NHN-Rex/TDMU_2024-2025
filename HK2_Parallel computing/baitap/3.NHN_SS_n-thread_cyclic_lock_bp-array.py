from threading import Thread, Lock
import time
lock = Lock()


def sq(arr, rs, id, lock, index):
    print(f"Waiting for Lock: Thread {id}")
    lock.acquire()
    print(f"Acquired Lock: Thread {id}")
    print(f"Thread {id}: arr[{index}] = {arr[index]} = {arr[index]**2}")
    rs.append(arr[index]**2)
    lock.release() 
    print(f"Release Lock: Thread {id}")

if __name__ == '__main__':
    rs = []
    n = int(input('Nhap so luong phan tu: '))
    arr = []
    threads = []
    num_threads = 4
    for i in range(n):
        arr.append(i+1)
    start = time.perf_counter()
    for i in range(n//num_threads):
        for j in range(num_threads):
            index = i*num_threads + j
            thread = Thread(target=sq, args=(arr, rs, j, lock, index))
            threads.append(thread)
            thread.start()
    for thread in threads:
        thread.join()
    rs.sort()
    print('Ket qua: ', rs)
    end = time.perf_counter()
    print('Thoi gian thuc hien la: ',end-start)