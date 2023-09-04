from threading import *

class buyticket:
    def __init__(self,availableseats):
        self.availableseats=availableseats
        self.l=Semaphore()


    def buy(self,requestedseats):
        self.l.acquire()
        print(self.availableseats)
        if(self.availableseats>=requestedseats):
            print("confirming the ticket")
            print("processing the payment")
            print("printing the ticket")
        else:
            print("Sorry ! No seats")
        self.availableseats-=requestedseats
        self.l.release()

obj=buyticket(10)
t1=Thread(target=obj.buy(3))
t2=Thread(target=obj.buy(4))
t3=Thread(target=obj.buy(4))

t1.start()
t2.start()
t3.start()
