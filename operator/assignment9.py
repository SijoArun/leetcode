x=int(input("Enter the number upto 100"))
for i in range(x):
    if(x>100):
        break
    elif (i % 10 == 0):
        continue
    print(i)



