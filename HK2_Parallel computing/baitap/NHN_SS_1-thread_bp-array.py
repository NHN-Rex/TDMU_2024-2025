import threading
import time

def bp(n):
    return n**2

def sq(data):
    for i in data:
        rs.append(bp(i))
    print("Mang sau khi binh phuong: ", rs)

# n = int(input('Nhap so luong phan tu: '))
n = 10
arr = []
rs = []
for i in range(n):
    arr.append(i+1)
print('Mang truoc khi binh phuong: ', arr)
start = time.time()
thread1 = threading.Thread(target=sq, args=(arr,))
thread1.start()
thread1.join()
end = time.time()
print('Thoi gian thuc hien la: ',end-start)