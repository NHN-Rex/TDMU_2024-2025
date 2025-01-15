# 2 cach tao thread


import threading 
import math

def target_func(data):
    thread_id = threading.get_ident()
    print('Thread {} is running with data: {}'.format(thread_id, data))

class WorkerThread(threading.Thread):
    def __init__(self, data):
        super().__init__()
        self.data = data
    def run(self):
        print('Thread {} is running with data: {}'.format(self.ident, self.data))



if __name__ == '__main__':
    a = 'Nguyen Huu Nghia'
    b = 'ABC'
    thread1 = threading.Thread(target=target_func, args=(a,))
    thread2 = WorkerThread(b)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print('Main thread exited')



