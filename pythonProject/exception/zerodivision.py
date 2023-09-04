try:
    a,b=[int(x) for x in input("Enter the two numbers").split()]
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Exception is due to zerodivision error , please enter the different number")
print("program continued after the exception")