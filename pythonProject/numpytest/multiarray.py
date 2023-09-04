from numpy import *

a1=array([1,2,3])
a2=array([[1,2,3],[4,5,6]])
a3=array([[[1,2],[3,4]],[[5,6],[7,8]]])

print(a1)
print(a2)
print(a3)

print(a1.ndim)
print(a2.ndim)
print(a3.ndim)

print(a1.shape)
print(a2.shape)
print(a3.shape)

print(a1.size)
print(a2.size)
print(a3.size)

print(a1.itemsize)
print(a2.itemsize)
print(a3.itemsize)

print(a1.dtype)
print(a2.dtype)
print(a3.dtype)