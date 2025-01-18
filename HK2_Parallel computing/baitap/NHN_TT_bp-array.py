import threading
import time

def bp(n):
    return n**2

start = time.time()
# n = int(input('Nhap so luong phan tu: '))
n = 1000
arr = []
rs = []

for i in range(n):
    arr.append(i+1)
print('Mang truoc khi binh phuong: ', arr)
for i in range(len(arr)):
    rs.append(bp(arr[i]))

print('Mang sau khi binh phuong: ',rs)
end = time.time()
print('Thoi gian thuc hien la: ',end-start)