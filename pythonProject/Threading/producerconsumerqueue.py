import random
from threading import *
import queue
import time

def producer(q):
    while True:
        print("producing")
        q.put(random.randint(1,50))
        print("produced")
        time.sleep(1)

def consumer(q):
    while True:
        print("Ready to consume")
        print("consume data ",q.get())
        time.sleep(1)

q=queue.Queue()
t1=Thread(target=consumer(q),args=(q,))
t1.start()

t2=Thread(target=producer(q),args=(q,))
t2.start()

