import numpy as np

arr = np.arange(25)

print(arr.shape)

print(arr.reshape(5,5))

print(arr.max())

print(arr.argmax()) # max ın index i 

print(arr.min())

print(arr.argmin()) # min in index i

print(arr.mean())

print(arr.sum())

print(arr.var())

print(arr.std())

print(arr.dtype)

arr2d = np.arange(20).reshape(5, 4)

print(arr2d)

print(np.vsplit(arr2d, 5))

print(np.vsplit(arr2d, [1,3]))

print(np.hsplit(arr2d, 2))