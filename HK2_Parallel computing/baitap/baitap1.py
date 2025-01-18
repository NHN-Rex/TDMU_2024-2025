import threading

def work(data):
    thread_id = threading.get_ident()
    print(f"thread id {thread_id}\nHi, my name is: {data}")

name = "Nguyen Huu Nghia"
thread = threading.Thread(target=work, name="My_thread1", args=(name,))
thread.start()