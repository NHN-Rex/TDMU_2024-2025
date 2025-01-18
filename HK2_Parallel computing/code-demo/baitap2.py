import threading
import time
start = time.time()
n = int(input('Nhap so luong phan tu: '))
arr = []
rs = []
def bp(n):
    return n**2

for i in range(n):
    arr.append(i+1)
print('Mang truoc khi binh phuong: ', arr)
for i in range(len(arr)):
    rs.append(bp(arr[i]))

print('Mang sau khi binh phuong: ',rs)
end = time.time()
print(end-start)