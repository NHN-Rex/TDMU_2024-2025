import threading
import time

def thread_function(n):
  global sq
  print(f'Bat dau sleep {i} giay')
  time.sleep(i)
  sq = n*n
  print(f'{t.name} da binh phuong {n} bang {sq} ' )
   
if __name__ == "__main__":
  time_start = time.time()
  threads = []
  for i in range(3):
    t = threading.Thread(target=thread_function, args=(5,))
    t.start()
    threads.append(t)

  for t in threads:
    t.join()

time_end = time.time()  
print(f'Thoi gian thuc hien la: {time_end - time_start} giay')
