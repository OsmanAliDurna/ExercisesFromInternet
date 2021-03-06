import numpy as np

arr = np.arange(0,11)

print(arr[8])

print(arr[-1])

print(arr[1:5])

print(arr[1::2])

print(arr[::2])

sliceOfArray = arr[0:3]

sliceOfArray[:] = 100

print(sliceOfArray)