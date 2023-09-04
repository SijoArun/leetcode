from numpy import *

a1=arange(1,13)

print(a1)

a2=reshape(a1,[2,6])

print(a2)

a3=a2.flatten()
print(a3)

print(eye(3))

print(ones((3,3),int))