str=input("Enter the text : ")
n=len(str)
value=""
while(n!=0):
    value=value+str[n-1]
    n=n-1
print("Converted text : ",value)
if(str==value):
    print("Given Text is palindrome")
else:
    print("Given Text is not palindrome")
