x=int(input("Enter the min number"))
y=int(input("Enter the max number"))

i=x
if(x%2==0):i+=1
while(i<=y):
    print(i)
    i+=2