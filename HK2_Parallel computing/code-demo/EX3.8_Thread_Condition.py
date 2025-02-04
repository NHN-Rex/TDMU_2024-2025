from threading import Thread, Condition
from time import sleep

items = []
condition = Condition()

class consumer(Thread):
  def __init__(self):
    Thread.__init__(self)

  def consume(self):
    global condition
    global items
    condition.acquire()
    if len(items) == 0:
      condition.wait(5)
      print("Consumer notify : no item to consume")
    else:
      items.pop()
      print("Consumer notify : consumed 1 item")
      print("Consumer notify : items to consume are "\
                  + str(len(items)))
    condition.notify()
    condition.release()
    
  def run(self):
    for i in range(0,20):
      sleep(10)
      self.consume()

class producer(Thread):
  def __init__(self):
    Thread.__init__(self)
    
  def produce(self):
    global condition
    global items
    condition.acquire()

    if len(items) == 10:
      condition.wait(5)
      print("Producer notify : items producted are "\
                  + str(len(items)))
      print("Producer notify : stop the production!!")
    else:
      items.append(1)
      print("Producer notify : total items producted "\
                  + str(len(items)))
    condition.notify()
    condition.release()

  def run(self):
    for i in range(0,20):
      sleep(2)
      self.produce()

if __name__ == "__main__":
  producer = producer()
  consumer = consumer()

  producer.start()
  consumer.start()

  producer.join()
  consumer.join()
