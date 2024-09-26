import numpy as np


array1 = np.array([[1,2,3,4], [5,6,7,8], [8,9,10,11], [1,3,5,7]])

# print max, mean, sum, and min of the array

print(np.max(array1), np.mean(array1), np.sum(array1), np.min(array1), )

# sum along axis
print(np.sum(array1, axis=0)) # along column
print(np.sum(array1, axis=1)) # along row

# this will do matrix multiplication
print(array1 @ np.transpose(array1))


print(np.sin(np.array([1,2,34,45,5])))


# returns the standard variation of ever sindle element, var also does the same but it is distance a number from the mean
print(np.array([1,2,3,20,44,45,46]).std())

# return the cumsum of an array, can also do that through axis 
print(np.array([1,2,3,4]).cumsum())