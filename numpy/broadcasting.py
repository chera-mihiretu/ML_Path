import numpy as np

# when matrix under go with unequal value or matrix dimention 

array1 = np.array([[1,2,3,4], [5,6,7,8], [8,9,10,11]])

# do the operation on every single value
print(array1 * 5)

array2 = np.array([1,2,5,4])
# if the rows are similar we will have all row summed up with this current row
print(array1 + array2)

