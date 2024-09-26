import numpy as np

from numpy.linalg import inv


array = np.arange(0, 40, 2, dtype=np.int64)


print(array.size)
# change into given dimention 
twoDArray = array.reshape(2, 2, -1)

print(twoDArray)

# change to 1d 

oneDimention = twoDArray.reshape(-1)

print(oneDimention)

# ravel also return 1d array, does not copy the arrat

print(twoDArray.ravel())

# return flatten of  2d array returns a copy
print(twoDArray.flatten())
print(twoDArray)


# swapaxes swap two axes 

print(np.array([[1,2],[3,4]]).swapaxes(0,1))