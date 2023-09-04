s="All the power is with in you"
print(s)
temp=s.split()
#print(temp)
i=len(temp)-1
result=[]
while i >= 0:
    result.append(temp[i])
    i=i-1
output=' '.join(result)
print(output)