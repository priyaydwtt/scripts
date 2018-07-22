import numpy as np
arr1 = np.array([[1,2,3],[4,5,6,]])

#created 2 -dimensional array so rank =2 ;rank is number of dimensions


#type of array object
print(type(arr1))

#numbe rof dimensions
print(arr1.ndim)

#shape of array
print(arr1.shape)

#size of array total elements of the array
print(arr1.size)

#type of element in the array
print(arr1.dtype)


#define type of the array

arr2=np.array([[1,2,3],[2,3,4,]],dtype='float')
print(arr2)


#you can create and array from list or tuple

arr3=np.array(((1,2,3),(4,5,6)), dtype='float')
print(arr3)

#ceating an array with all zeroes
arr4=np.zeros((3,4))
print(arr4)

#create an array with complex type value
arr5=np.full((3,3),6,dtype='complex')
print(arr5)

#create an array with random number a 2x2 array
arr6=np.random.random((2,2))
print(arr6)

#create a seqential array with difference 5

arr7=np.arange(0,30,5)
print(arr7)

arr8=np.linspace(0,5,10)
print(arr8)


#slicing arrays

#:n - this means from index '0' to index 'n'
#::n - this means from '0' to index 'n' but all alternate indices

sarr1=arr1[::2,::2]
print("sarr1",sarr1)

#integer array indexing
sarr2 = arr1[[0,1],[1,0]]
print("integer array indexing",sarr2)

studdata= [('aravind',1998,78),('bala',1996,75),('chitra',2000,80)]
dtypes = [('name','S10'),('yop',int),('cgpa','float')]
#create an array with student name,graduation year and cgpa
studarr=np.array(studdata,dtype =dtypes)

print("sort using name",np.sort(studarr,order=['yop','cgpa']))









