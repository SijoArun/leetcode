try:
    f=open("myfile","w")
    a,b=[int(x) for x in input("Enter the two numbers").split()]
    c=a/b
    f.write("write into file %d"%c)
except ZeroDivisionError:
    print("Exception is due to zerodivision error , please enter the different number")
else:
    print("you have not entered non zero number")
finally:
    f.close()
    print("File is closed")
print("program continued after the exception")