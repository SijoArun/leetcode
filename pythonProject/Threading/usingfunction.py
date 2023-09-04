import threading
from threading import *

def displaynum():
    i=1
    print(threading.current_thread())
    while (i<=10):
        print(i)
        i+=1
print(threading.current_thread())
t=Thread(target=displaynum)
t.start()
