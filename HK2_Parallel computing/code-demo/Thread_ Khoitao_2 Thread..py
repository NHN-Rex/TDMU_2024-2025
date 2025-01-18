import threading
import time

# Hàm thực hiện tác vụ trong mỗi thread
def print_numbers(thread_name, count):
    for i in range(count):
        time.sleep(1)  
        print(f"{thread_name} đang in số: {i}")

# Tạo các thread
thread1 = threading.Thread(target=print_numbers, args=("Thread-1", 5))
thread2 = threading.Thread(target=print_numbers, args=("Thread-2", 2))

# Bắt đầu các thread
thread1.start()
thread2.start()

# Chờ các thread kết thúc
thread1.join()
thread2.join()

print("Tất cả các thread đã hoàn thành.")
