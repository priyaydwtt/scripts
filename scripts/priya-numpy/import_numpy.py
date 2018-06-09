import numpy as np
a=np.array([[1,2,],[3,4]])

print(a)

print(dir(a))

b=np.array([1,2,"a","b",],ndmin=2)

print(b)

print(b.size)

c=np.array([1,2,3,4,],dtype='complex')

print(c)

d=np.array([1.5,2.75,3.47,1.42],dtype='complex')

print(d)

#TypeError: must be real number, not str


