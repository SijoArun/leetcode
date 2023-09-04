s="aaaawqwqwqvvv"
temp=[]
for c in s:
    if c not in temp:
        temp.append(c)
output=''.join(temp)
print(output)