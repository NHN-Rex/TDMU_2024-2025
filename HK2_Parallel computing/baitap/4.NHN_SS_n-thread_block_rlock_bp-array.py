from threading import Thread, RLock
import time
rlock = RLock()
def bp(arr, rlock, name):
    print(f"Function bp: {name} Waiting for rLock bp")
    rlock.acquire()
    print(f"Acquired rLock bp: {name}")
    print(f"Function bp: {name} Executing Code bp....")
    for i in range(len(arr)):
        arr[i] = arr[i]**2
    time.sleep(1)
    rlock.release()
    print(f"Function bp: {name} Releases rLock bp")
    return arr
    


def sq(arr,rs, name, rlock):
    print(f"Function sq: {name} waiting for rLock sq")
    rlock.acquire()
    print(f"Acquired rLock sq: {name}")
    print(f"Function sq: {name} Executing Code sq....")
    # rs.append(bp(arr, rlock, name))
    rs+=bp(arr, rlock, name)
    # time.sleep(1)
    print(f"Mang sau binh phuong sau khi {name} chay: ", rs)
    rlock.release()
    print(f"Function sp: {name} Releases rLock sq")

if __name__ == '__main__':

    rs = []
    # n = 10
    n = int(input('Nhap so luong phan tu: '))
    arr = []
    num_threads = int(input('Nhap so luong thread: '))
    list_threads = []
    num_block = n//num_threads

    for i in range(n):
        arr.append(i+1)
    start = time.perf_counter()

    for thread_id in range(num_threads):
        start_index = thread_id * num_block
        end_index = start_index + num_block
        thread = Thread(target=sq, args=(arr[start_index:end_index], rs, thread_id, rlock))
        list_threads.append(thread)
        thread.start()
    for thread in list_threads:
        thread.join()
    end = time.perf_counter()
    print('Thoi gian thuc hien la: ',end-start)