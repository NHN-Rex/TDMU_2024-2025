# lay thong tin cua thread

import threading
def ham(n):
    n += 1
    print(f'Gia tri cua n la: {n}')

n = 10
my_thread = threading.Thread(target=ham, name='My_thread', args=(n, ))
my_thread.start()

print('ID cua thread: '+str(my_thread.native_id))
print('Ten cua thread: '+str(my_thread.name))

print('Tong so thread dang hoat dong la: '+str(threading.active_count()))
print('Ten cua thread chinh la: '+str(threading.main_thread()))
print('List cac thread dang hoat dong: '+str(threading.enumerate()))
my_thread.join()