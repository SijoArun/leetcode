import queue
from threading import Thread


class queuedef():
    def __init__(self,pq):
        self.pq=pq

    def evenadd(self):
        for i in range(1,101):
            if(( i % 2) ==0):
                self.pq.put(i)
        print("Even addition is completed")

    def oddadd(self):
        for i in range(0, 101):
            if ((i % 2) == 1):
                self.pq.put(i)
        print("Odd addition is completed")



pq=queue.PriorityQueue()
qd=queuedef(pq)
t1=Thread(target=qd.evenadd())
t2=Thread(target=qd.oddadd())

while not pq.empty():
    print(pq.get(),end=' ')