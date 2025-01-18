import threading

def ham(n):
  global bien
  n += 1
  # Lay ten thread
  print('Cach 1: Ten cua thread la ' + my_thread.name)
  print('Cach 2: Ten cua thread la ' + threading.current_thread().name)
  print('ID cua thread ' + str(my_thread.native_id))
  # Lay so ID cua thread
  print('So ID cua thrad la ' + str(my_thread.native_id))
  # Ma dinh danh cua thread
  print('Ident cua thread ' + str(my_thread.ident))
  print(f'Gia tri cua n la: {n} ')

n = 10
mythreads = ["MyThread1", "MyThread2"]
for i in range(2):
  my_thread = threading.Thread(target = ham, name = mythreads[i], args = (n,))
  my_thread.start()

# Module threading
print('Tong so thread dang hoạt dong la: ' + str(threading.active_count()))
print('Ten Thread chinh la: ' + str(threading.main_thread()))
print('List cac thread dang hoat dong: ' + str(threading.enumerate()))

for i in range(2):
  my_thread.join()
