import threading

print("current thread",threading.current_thread())

if (threading.current_thread()==threading.main_thread()):
    print("main thread is running")
else:
    print("some other thread")