import threading
from threading import *
from time import sleep


class MyThread():
    def displaynum(self):

        i = 1
        print(threading.current_thread())
        sleep(1)
        while (i <= 10):
            print(i,"\n")
            i += 1

obj=MyThread()
t=Thread(target=obj.displaynum)
t.start()

t2=Thread(target=obj.displaynum)
t2.start()

t3=Thread(target=obj.displaynum)
t3.start()