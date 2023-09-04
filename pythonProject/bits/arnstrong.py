num = str(input("Enter a number : "))
n = (len(num))
result=int(1)
no=int(0)
calculateno=int(0)
for base in num:
    expo = int(n)
    result = 1
    while (expo!=0):
        result = result * int(base)
        expo=expo-1
    no = 0 + result
    calculateno=calculateno+no
print("calculated no : ",calculateno)
if(calculateno==(int(num))):
    print("Number is armstrong")
else:
    print("Number is not armstrong")
