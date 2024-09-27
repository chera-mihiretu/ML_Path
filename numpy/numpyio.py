import numpy as np 
array = []

array1 = np.arange(0, 100, 2)

# saving into npy file
np.save('aray.npy', array1)

# sacing into txt file
np.savetxt('array.txt', array1, delimiter=',')

# saving multiple array
np.savez('array.npz', array1=array1)


# loading from file txt

load_txt = np.genfromtxt('array.txt', delimiter=',', filling_values=np.nan)

print(load_txt)

# loading from npy

load_npy = np.load('aray.npy')

print(load_npy)

# load from npz 
load_npz = np.load('array.npz')

print(load_npz['array1'])