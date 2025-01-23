from threading import Thread, Lock
import time

def bp(n):
    return n**2

lock = Lock()
def sq(data, name, lock):
    print(f"Thread {name}: ", end='')
    print("Waiting for Lock: " + name)
    rs = []
    lock.acquire()
    for i in data:
        rs.append(bp(i))
    print("Mang sau khi binh phuong: ", rs)
    lock.release()
    print("Released Lock")
if __name__ == '__main__':
    n = 10
    arr = []
    for i in range(n):
        arr.append(i+1)
    start = time.perf_counter()
    thread1 = Thread(target=sq, args=(arr[:int(len(arr)/2)], 'Thread 1', lock))
    thread2 = Thread(target=sq, args=(arr[int(len(arr)/2):], 'Thread 2', lock))
    thread1.start()
    thread2.start()

    thread2.join()
    thread1.join()
    end = time.perf_counter()
    print('Thoi gian thuc hien la: ',end-start)