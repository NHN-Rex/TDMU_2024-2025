# tao 2 thread

import threading
import time

def thread1(i):
    time.sleep(3)
    print('No. Printed by Thread 1:', i)

def thread2(i):
    time.sleep(5)
    print('No. Printed by Thread 2:', i)


if __name__ == '__main__':
    t1 = threading.Thread(target=thread1, args=(10, ))
    t2 = threading.Thread(target=thread2, args=(12, ))

    t1.start()
    t2.start()
    t1.join()
    t2.join()