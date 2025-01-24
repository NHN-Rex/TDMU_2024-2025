from threading import Thread, Semaphore
import time
semaphore = Semaphore(3)

def sq(arr, rs, name):
     
    print(f"Thread {name} is waiting for his turn")
    semaphore.acquire()
    
    print(f"Thread {name} is playing")
    rs.append(arr[name]**2)
    
    print(f"Thread {name} has left the playground")
    semaphore.release()

if __name__ == '__main__':

    rs = []
    # n = 10
    n = int(input('Nhap so luong phan tu: '))
    arr = []
    for i in range(n):
        arr.append(i+1)
    start = time.perf_counter()
    children = []

    for i in range(n):
        children.append(Thread(target=sq, args = (arr, rs, i, )))
        children[i].start()

    for i in range(n):
        children[i].join()
    rs.sort()
    print('ket qua: ', rs)
    end = time.perf_counter()
    print('Thoi gian thuc hien la: ',end-start)