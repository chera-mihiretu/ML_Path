import numpy as np

array1 = np.array([[1 + i,2 + i,3 + i,4 + i,5 + i] for i in range(5)])
# print row and col sliced
print(array1[1:3, 2:4]) # column row 
print(array1)

# reshaping into 2d
array2 = np.arange(0, 20, 2).reshape(3,3)

print(array2)