from random import *

for i in range(5):
    print(random())

for i in range(5):
    print(randint(1,5))

    for i in range(5):
        print(randrange(1, 5,2))

lst=["java","python","aws"]

for i in range(0,5):
    print(choice(lst))