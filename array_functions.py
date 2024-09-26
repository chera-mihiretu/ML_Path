import numpy as np

# identity matrix [1,0,0], [0,1,0], [0,0,1]
array1 = np.eye(4)
print(array1)

#fill the matric with zeros
array2 = np.zeros((4,4))

print(array2)
# fill the array with specific value
array6 = np.full((3,4), 8)
print(array6)
# fill the matrix with one
array3 = np.ones((3,4))
array4 = np.ones((3,4))
print(array3)
print(array3 + array4)


array5 = np.arange(10, 40, 5.3)

# return the byte of the array
print(array5.nbytes)
# returns the byte of each element 
print(array5.itemsize)

# returns the dtype type of elemtn
print(array5.dtype)

# return matrix with the given shape filled with random numbers

array7 = np.empty((4,4), dtype=np.float32)
print(array7)

#generate random arrays
print(np.random.randint(1, 9))

