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
# n = int(input('Nhap so luong phan tu: '))
n = 10
arr = []
for i in range(n):
    arr.append(i+1)
start = time.time()
thread1 = Thread(target=sq, args=(arr[:int(len(arr)/2)], 'T1', lock,))
thread2 = Thread(target=sq, args=(arr[int(len(arr)/2):], 'T2',lock))
thread1.start()
thread2.start()

thread2.join()
thread1.join()
end = time.time()
print('Thoi gian thuc hien la: ',end-start)