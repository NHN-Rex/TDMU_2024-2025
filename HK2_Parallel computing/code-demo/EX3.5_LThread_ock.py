from threading import Thread, Lock
from time import sleep

lock = Lock()

def square_cubic(mylist,yourlist,p,namethread,lock):
  print("Waiting for Lock: " + namethread)
  lock.acquire()
  print("Acquired Lock: " + namethread)
  # Thuc hien cong viec
  print('Dang chay la ' + namethread)
  for i in mylist:
    yourlist.append(i ** p)
    sleep(1)
  lock.release()
  print("Released Lock")

if __name__ == "__main__":
  mylist = [1,2,3,4,5,6,7,8,9,10]
  yourlist = []

  t1 = Thread(target=square_cubic, args=(mylist,yourlist,2,'thread 1',lock))
  t2 = Thread(target=square_cubic, args=(mylist,yourlist,3,'thread 2',lock))
  t1.start()
  t2.start()

  t1.join()
  t2.join()
  print('Yourlist: ' + str(yourlist))
