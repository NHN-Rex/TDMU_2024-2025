import threading
import time
import random

items = []
event = threading.Event()

class Consumer(threading.Thread):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  def run(self):
    while True:
      time.sleep(2)
      e = event.wait()
      if e:
        if len(items) != 0:
          item = items.pop()
          print('Consumer notify: {} popped by {}'\
                .format(item, self.name))
        else:
          print('Consumer notify: Time out!')
      if event.is_set():
        break
          
class Producer(threading.Thread):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  def run(self):
    global item
    global np
    time.sleep(1)
    print('Producer notify: Start product output item!')
    item = random.randint(1, 100)
    items.append(item)
    print('Producer notify: item {} appended by {}'\
                .format(item, self.name))
    event.set()
    time.sleep(5)
    event.clear()
    
if __name__ == "__main__":
  t1 = Producer()
  t2 = Consumer()
  t1.start()
  t2.start()
  t1.join()
  t2.join()
  print('Done!')
