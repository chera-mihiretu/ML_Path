import numpy as np


oneDarray = np.array([1,2,3,4,5])

print(oneDarray)

# print elements separatedd by the given argument as 3rd value [0.5]
print('[ARANGE]',*np.arange(0, 10, .5), sep=' ')

# list num number of elements separated by evenly distributed values
print(['LINESPACE'],*np.linspace(0, 5, num=10), sep='\n')


# initialize numpy array
arr  = np.array([1,2,3,4])

# add the number to all list values
print('[ARR + 4]',arr, arr + 4) # any operation will be done on every single value {/ * + -}

print('[ARR * 9]',arr * 9)

# print square root of every single vals
print(np.sqrt(arr))
# exponatiate of all arr
print(np.exp(arr))

