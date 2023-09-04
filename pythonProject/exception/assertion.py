try:
    num=int(input("Enter a even number"))
    assert num%2==0,"Wrong input ! please enter the valid number"
except AssertionError as obj:
    print(obj)
print("Program continued !!!!")
