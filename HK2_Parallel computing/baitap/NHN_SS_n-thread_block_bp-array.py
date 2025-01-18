import threading
import time

def bp(n):
    return n**2

def sq(data, name):
    print(f"Thread {name}: ", end='')
    rs = []
    for i in data:
        rs.append(bp(i))
    print("Mang sau khi binh phuong: ", rs)
# n = int(input('Nhap so luong phan tu: '))
n = 10
arr = []
for i in range(n):
    arr.append(i+1)
    
start = time.time()
thread1 = threading.Thread(target=sq, args=(arr[:int(len(arr)/2)], 'T1'))
thread2 = threading.Thread(target=sq, args=(arr[int(len(arr)/2):], 'T2'))
thread1.start()
thread2.start()

thread2.join()
thread1.join()
end = time.time()
print('Thoi gian thuc hien la: ',end-start)