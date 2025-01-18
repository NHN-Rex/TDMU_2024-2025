import threading
import time

class PrintNumbersThread(threading.Thread):
    def __init__(self, name, counter, delay):
        super(PrintNumbersThread, self).__init__()
        self.name= name
        self.counter=counter
        self.delay= delay
    
    def run(self):
        for i in range(1, self.counter):
            print(i)
            print(f"Ten cua thread la {self.name}")
            time.sleep(self.delay)

# Tạo và khởi chạy thread
counter = 5
delay = 2
thread = PrintNumbersThread("thread 1", counter, delay)
thread.start()

# Đợi thread hoàn thành
thread.join()

print("Thread da hoan thanh.")