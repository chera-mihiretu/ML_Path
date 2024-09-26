import numpy as np

array = np.array([1,2,3,np.nan, 5,6])

print(array)

# to check if one of the array is nan

print(any(np.isnan(array)))


# we can remove the nan 
# this works by creating the mask of the boolean values of the values where false is returned for the nan
print(array[~np.isnan(array)])

# we can replace the nan
print(np.nan_to_num(array, nan=4))

# whenever doing operation on nan array we use the nan before the operation function 

print(np.nanmean(array))

# infinity are also treated as nan

# we can check infarrays as

array2 = np.array([1,2,3, np.inf, -np.inf, 6, 7])

print(np.isinf(array2))

# replacing the inf vals
print(np.nan_to_num(array2, posinf=1, neginf=-1))