from numpy import *

a1=array([1,2,3,4])
a2=array([60,70,80,90])

print(a1>=a2)
print(a1<=a2)

print(any(a1>=a2))
print(all(a1>=a2))

print(logical_and(a1>=10,a1<100))
print(logical_or(a1>10,a1<100))

print(where(a1%2!=0,a1,0))
print(where(a1>a2,a1,a2))