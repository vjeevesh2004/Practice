import numpy as np 

a = np.array([1,2,3])
b = np.array([4,5,6])

print("Additon: ", a + b)

z = np.array([4,9,25,16])
print("Square root: ", np.sqrt(z))
print("Exponential: ", np.exp(z))

# reshapping

ar = np.array([1,2,3,4,5,8,9,5]) # even num of elements
reshape = ar.reshape((4,2)) # (row column) row column = no. of element in array
print("Reshaped array : \n", reshape)

# transpose

a_2d = np.array([[1,2,3], [4,5,6]])
print("Transposed array:\n", a_2d.T)

# using all methods
a = np.arange(6).reshape((2,3))
print(a)
b=np.transpose(a)
print(b)

