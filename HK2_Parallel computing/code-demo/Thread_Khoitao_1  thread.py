import threading

def print_numbers(n):
    for i in range(1, n):
        print(i)

# Tạo một đối tượng Thread
thread = threading.Thread(target=print_numbers, args =(5,))

# Khởi chạy thread
thread.start()

# Đợi thread hoàn thành
thread.join()

print("Thread da hoan thanh.")