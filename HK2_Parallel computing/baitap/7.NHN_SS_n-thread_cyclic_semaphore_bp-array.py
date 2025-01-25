from threading import Thread, Semaphore
import time
semaphore = Semaphore(3)

def sq(arr, rs, index, thread_id):
     
    print(f"Thread {thread_id} is waiting for his turn")
    semaphore.acquire()
    
    # print(f"Thread {thread_id} is playing and semaphore: {semaphore._value}")
    # print(f"Semaphores: {semaphore._value}")
    rs.append(arr[index]**2)
    time.sleep(1)
    
    semaphore.release()
    # print(f"Thread {thread_id} has left the playground and semaphore: {semaphore._value}")

if __name__ == '__main__':

    rs = []
    # n = 10
    n = int(input('Nhap so luong phan tu: '))
    arr = []
    list_threads = []
    num_threads = int(input('Nhap so luong thread: '))
    for i in range(n):
        arr.append(i+1)
    start = time.perf_counter()

    # print(f"First Semaphores: {semaphore._value}")
    for i in range(n//num_threads):
        for j in range(num_threads):
            index = i*num_threads + j
            list_threads.append(Thread(target=sq, args=(arr, rs, index, j)))
            list_threads[index].start()

    for thread in list_threads:
        thread.join()
    rs.sort()
    # print(f"Last Semaphores: {semaphore._value}")
    print('ket qua: ', rs)
    end = time.perf_counter()
    print('Thoi gian thuc hien la: ',end-start)