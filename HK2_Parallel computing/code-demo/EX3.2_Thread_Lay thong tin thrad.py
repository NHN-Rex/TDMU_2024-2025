import threading

def ham(n):
  global bien
  n += 1
  print(f'Gia tri cua n la: {n} ')

n = 10
my_thread = threading.Thread(target = ham, name = 'MyThread', args = (n,))
my_thread.start()

# Lay ID cua thread
print('ID cua thread ' + str(my_thread.native_id))

# Lay ten thread
print('Ten cua thread la ' + my_thread.name)

# Lay so ID cua thread
print('So ID cua thrad la ' + str(my_thread.native_id))

# Ma dinh danh cua thread
print('Ident cua thread ' + str(my_thread.ident))

# Module threading
print('Tong so thread dang hoạt dong la: ' + str(threading.active_count()))
print('Ten Thread chinh la: ' + str(threading.main_thread()))
print('List cac thread dang hoat dong: ' + str(threading.enumerate()))

my_thread.join()
