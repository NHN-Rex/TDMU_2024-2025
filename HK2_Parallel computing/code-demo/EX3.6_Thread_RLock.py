from threading import Thread, RLock
from time import sleep
 
rlock = RLock()
 
def func_2(rlock, name):
  print("Function 2: " + name + " Waiting for rLock")
  rlock.acquire()
  print("Function 2: " + name + " Executing Code....")
  sleep(1)
 
  rlock.release()
  print("Function 2: " + name + " Releases rLock")
 
def func_1(rlock, name):
  print("Function 1: " + name + " Waiting for rLock")
  rlock.acquire()
 
  print("Function 1: " + name + " Executing Code....")
  func_2(rlock, name)
 
  rlock.release()
  print("Function 1: "+ name + " Releases rLock")
 
t1 = Thread(target= func_1, args= (rlock,'Thread 1'))
t2 = Thread(target= func_1, args= (rlock,'Thread 2'))
t1.start()
t2.start()

t1.join()
t2.join()
