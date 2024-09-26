import numpy as np

array1 = np.array([1,2,3,4])
array2 = np.array([1,1,1,1])
#stack the arrays row wise or col wise based on axis axis=0 is row wise 
stack = np.stack((array1, array2), axis=1)

print(stack)

# stack the arrays horizontally

print(np.hstack((array1, array2)))

# stack the arrays vertically
print(np.vstack((array1, array2)))

#split rows into single array
print(np.hsplit(stack, 2))

#split cols into single array
print(np.vsplit(stack, 2))


