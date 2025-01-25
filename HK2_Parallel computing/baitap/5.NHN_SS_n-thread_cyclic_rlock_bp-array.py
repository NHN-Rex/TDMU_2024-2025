from threading import Thread, RLock
import time
rlock = RLock()
def bp(arr, index, rlock, name):
    print("Function bp: " + name + " Waiting for rLock bp")
    rlock.acquire()
    print("Acquired rLock bp: " + name)
    print("Function bp: " + name + " Executing Code bp....")
    arr[index] = arr[index]**2
    time.sleep(1)
    rlock.release()
    print("Function bp: " + name + " Releases rLock bp")
    return arr[index]
    


def sq(arr,index,rs, name, rlock):
    print("Function sq: " + name + " waiting for rLock sq")
    rlock.acquire()
    print("Acquired rLock sq: " + name)
    print("Function sq: " + name + " Executing Code sq....")
    # rs.append(bp(arr, rlock, name))
    rs.append(bp(arr, index, rlock, name))
    time.sleep(1)
    # rs.sort()
    print(f"Mang sau binh phuong sau khi {name} chay: ", rs)
    rlock.release()
    print("Function bp: " + name + " Releases rLock sq")

if __name__ == '__main__':

    rs = []
    # n = 10
    n = int(input('Nhap so luong phan tu: '))
    numthreads = int(input('Nhap so luong thread: '))
    arr = []
    threads = []
    for i in range(n):
        arr.append(i+1)
    start = time.perf_counter()
    for i in range(n//numthreads):
        for j in range(numthreads):
            index = i*numthreads + j
            thread = Thread(target=sq, args=(arr, index, rs, f'Thread {j}', rlock))
            threads.append(thread)
            thread.start()
    for thread in threads:
        thread.join()
    end = time.perf_counter()
    print('Thoi gian thuc hien la: ',end-start)