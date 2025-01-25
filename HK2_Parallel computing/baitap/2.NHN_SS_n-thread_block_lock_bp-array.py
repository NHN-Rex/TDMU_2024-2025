from threading import Thread, Lock
import time
lock = Lock()
def bp(n):
    return n**2


def sq(arr,rs, name, lock):
    print("Waiting for Lock: " + name)
    lock.acquire()
    print("Acquired Lock: " + name)
    print('Is running: ' + name)
    for i in arr:
        rs.append(bp(i))
    time.sleep(1)
    print(f"Mang sau binh phuong sau khi {name} chay: ", rs)
    lock.release()
    print(f"Released Lock: {name}")

if __name__ == '__main__':

    rs = []
    # n = 10
    n = int(input('Nhap so luong phan tu: '))
    arr = []
    for i in range(n):
        arr.append(i+1)
    start = time.perf_counter()
    thread1 = Thread(target=sq, args=(arr[:int(len(arr)/2)],rs, 'Thread 1', lock))
    thread2 = Thread(target=sq, args=(arr[int(len(arr)/2):],rs, 'Thread 2', lock))
    thread1.start()
    thread2.start()

    thread2.join()
    thread1.join()
    end = time.perf_counter()
    print('Thoi gian thuc hien la: ',end-start)