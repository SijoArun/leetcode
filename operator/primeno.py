x = int(input("Given no prime or not"))
n = range(2, x )
primeflag = False
for i in n:
    if (x % i == 0):
        primeflag = True
if (primeflag):
    print("Not a prime ",x)
else :
    print("prime no",x)

