from threading import Thread, RLock
import time
rlock = RLock()
def bp(arr, start, rlock, name):
    print("Function bp: " + name + " Waiting for rLock bp")
    rlock.acquire()
    print("Acquired rLock bp: " + name)
    print("Function bp: " + name + " Executing Code bp....")
    for i in range(start, len(arr), 2):
        arr[i] = arr[i]**2
    rlock.release()
    print("Function bp: " + name + " Releases rLock bp")
    return arr
    


def sq(arr,start,rs, name, rlock):
    print("Function sq: " + name + " waiting for rLock sq")
    rlock.acquire()
    print("Acquired rLock sq: " + name)
    print("Function sq: " + name + " Executing Code sq....")
    # rs.append(bp(arr, rlock, name))
    rs=bp(arr, start, rlock, name)
    # rs.sort()
    print(f"Mang sau binh phuong sau khi {name} chay: ", rs)
    rlock.release()
    print("Function bp: " + name + " Releases rLock sq")

if __name__ == '__main__':

    rs = []
    # n = 10
    n = int(input('Nhap so luong phan tu: '))
    arr = []
    for i in range(n):
        arr.append(i+1)
    start = time.perf_counter()
    thread1 = Thread(target=sq, args=(arr, 0, rs, 'Thread 1', rlock))
    thread2 = Thread(target=sq, args=(arr, 1, rs, 'Thread 2', rlock))
    thread1.start()
    thread2.start()

    thread2.join()
    thread1.join()
    end = time.perf_counter()
    print('Thoi gian thuc hien la: ',end-start)