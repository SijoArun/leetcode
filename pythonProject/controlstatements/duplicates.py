l1=eval(input("Enter the list of elements"))
l2=[]
for each_value in l1:
    if each_value not in l2:
        l2.append(each_value)
print(l2)

s1=set(l1)
print(s1)