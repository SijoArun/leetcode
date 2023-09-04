a=[1,2,3,4,5]
b=[6,7,8,9,10]

p=[]
"""for i in range(len(a)):
    p.append(a[i]*b[i])
    """
p=[a[i]*b[i] for i in range(len(a))]
print(p)
