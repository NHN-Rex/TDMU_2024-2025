from threading import Thread, Semaphore
import time
semaphore = Semaphore(3)

def sq(arr, rs, thread_id):
     
    print(f"Thread {thread_id} is waiting for his turn")
    semaphore.acquire()
    
    print(f"Thread {thread_id} is playing")
    for i in arr:
        rs.append(i**2)
    time.sleep(1)
    
    print(f"Thread {thread_id} has left the playground")
    semaphore.release()

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
        thread = Thread(target=sq, args=(arr[start_index:end_index], rs, thread_id,))
        list_threads.append(thread)
        thread.start()

    for thread in list_threads:
        thread.join()

    rs.sort()
    print('ket qua: ', rs)
    end = time.perf_counter()
    print('Thoi gian thuc hien la: ',end-start)