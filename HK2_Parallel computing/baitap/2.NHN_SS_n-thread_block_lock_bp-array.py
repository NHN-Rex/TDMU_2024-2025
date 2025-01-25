from threading import Thread, Lock
import time
lock = Lock()

def bp(n):
    return n**2


def sq(arr,rs, thread_id, lock):
    print(f"Waiting for Lock: Thread {thread_id}")
    lock.acquire()
    print(f"Acquired Lock: Thread {thread_id}")
    print(f'Is running: Thread {thread_id}')
    for i in arr:
        rs.append(bp(i))
    # time.sleep(1)
    print(f"Mang sau binh phuong sau khi Thread {thread_id} chay: ", rs)
    lock.release()
    print(f"Released Lock: Thread {thread_id}")

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
        start_index = thread_id*num_block
        end_index = start_index + num_block
        thread = Thread(target=sq, args=(arr[start_index:end_index], rs, thread_id, lock))
        list_threads.append(thread)
        thread.start()
    
    for thread in list_threads:
        thread.join()

    end = time.perf_counter()
    print('Thoi gian thuc hien la: ',end-start)