from threading import Thread, Semaphore
import time
semaphore = Semaphore(2)
def bp(arr):
    for i in range(start, len(arr), 2):
        arr[i] = arr[i]**2
    return arr
    


def sq(arr, rs, name, start, end):
    print("Function sq: " + name + " waiting for rLock sq")
    semaphore.acquire()
    print("Acquired rLock sq: " + name)
    print("Function sq: " + name + " Executing Code sq....")
    # rs.append(bp(arr, rlock, name))
    rs=bp(arr)
    # rs.sort()
    print(f"Mang sau binh phuong sau khi {name} chay: ", rs)
    semaphore.release()
    print("Function bp: " + name + " Releases rLock sq")

if __name__ == '__main__':

    rs = []
    # n = 10
    n = int(input('Nhap so luong phan tu: '))
    arr = []
    for i in range(n):
        arr.append(i+1)
    start = time.perf_counter()
    children = []

    for i in range(10):
        children.append(Thread(target=sq, args = (arr, rs, f'Thread {i}', )))
        children[i].start()

    for i in range(10):
        children[i].join()
    end = time.perf_counter()
    print('Thoi gian thuc hien la: ',end-start)