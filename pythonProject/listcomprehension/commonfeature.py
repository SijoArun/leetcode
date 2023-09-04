a=[2,4,6]
b=[5,2,4]

result=[]
'''
for i in a:
    if i in b:
        result.append(i)
        '''
result=[i for i in a if i in b]
print(result)