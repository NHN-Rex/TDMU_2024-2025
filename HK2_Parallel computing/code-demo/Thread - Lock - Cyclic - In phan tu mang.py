import threading
import time
mylock = threading.Lock()

# ********************** CACH 1: CHIA CÔNG VIỆC TRONG HÀM def ****************************************
# SỬ DỤNG with lock
# def in_phan_tu_mang(arr, thread_id, num_threads, lock):
#     """Hàm in các phần tử của mảng theo phân hoạch vòng tròn (cyclic)"""
#     for i in range(thread_id, len(arr), num_threads):
#         with lock:  # Đảm bảo chỉ một luồng in tại một thời điểm
#             print(f"Thread {thread_id}: arr[{i}] = {arr[i]}")

# Sử dụng : lOCK
# def in_phan_tu_mang(arr, thread_id, num_threads, lock):
#     """Hàm in các phần tử của mảng theo phân hoạch vòng tròn (cyclic)"""
#     for i in range(thread_id, len(arr), num_threads):
#         lock.acquire() # Đảm bảo chỉ một luồng in tại một thời điểm
#         print(f"Thread {thread_id}: arr[{i}] = {arr[i]}")
#         lock.release() 

# n = 20
# arr = [i for i in range(n)]  # Mảng gồm n phần tử từ 0 đến n-1
# num_threads = 4  # Sử dụng 4 luồng
# threads = []

# for thread_id in range(num_threads):
#     thread = threading.Thread(target=in_phan_tu_mang, args=(arr, thread_id, num_threads, mylock))
#     threads.append(thread)
#     thread.start()
# for thread in threads:
#     thread.join()


# ********************** CACH 2: CHIA CÔNG VIỆC TRƯỚC KHI GỌI HÀM def ****************************************
def in_phan_tu_mang(arr, index,thread_id, mylock):
    #time.sleep(0.01) 
    mylock.acquire() # Đảm bảo chỉ một luồng in tại một thời điểm
    #print(f"Thread {thread_id} giu duoc khoa")
    print(f"Thread {thread_id}: arr[{index}] = {arr[index]}")
    mylock.release() 
    #print(f"Thread {thread_id} da tra khoa")

n = 20
arr = [i for i in range(n)]  # Mảng gồm n phần tử từ 0 đến n-1
num_threads = 4  # Sử dụng 4 luồng
threads = []

#  Từng thread thực hiện công việc xong công việc.
# for thread_id in range(num_threads):
#     for i in range(thread_id, len(arr), num_threads):
#         index = i # phân chia công việc
#         thread = threading.Thread(target=in_phan_tu_mang, args=(arr, index,thread_id, mylock))
#         threads.append(thread)
#         thread.start()

#  Trong 1 chu kỳ có cả các thrad thực hiện công việc, mỗi thread thực hiện 1 công việc.
m = n//num_threads 
for i in range(m):
    for thread_id in range(num_threads):
        index = i*num_threads + thread_id # phân chia công việc
        thread = threading.Thread(target=in_phan_tu_mang, args=(arr, index,thread_id, mylock))
        threads.append(thread)
        thread.start()
for thread in threads:
    thread.join()
