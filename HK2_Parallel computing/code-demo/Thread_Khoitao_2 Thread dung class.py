from threading import Thread
import time

class myThread(Thread):
    def __init__(self, name, counter, delay):
        super(myThread, self).__init__()
        self.name= name
        self.counter=counter
        self.delay=delay

    def run(self):
        print("San sang chay " + self.name)
        for i in range(self.counter):
            time.sleep(self.delay)
            print(f"{self.name} dang in so: {i}")
        print("Ket thuc vong lap:", self.name)

thread1 = myThread("thread 1", 10, 1)
thread2 = myThread("thread 2", 10, 3)
thread1.start()
thread2.start()
#thread1.join()
#thread2.join()
print("Hai thread da hoan thanh!")

