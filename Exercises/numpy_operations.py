import numpy as np

arr = np.arange(1,11)

print(arr)

print(arr>4)

bool_arr = arr > 4

print(bool_arr)

print(arr[bool_arr])

print(arr[arr>4])

print(arr[(arr>4) & (arr<8)])

print(arr+arr)

print(arr**2)

print(arr%arr)

v = np.array([1, 2, 3, 4, 5])

print(v-1)

print(v*5)

print(v[1:3]+2)

print(np.sqrt(arr).round(3))

print(np.square(arr))

print(np.exp(arr))

print(np.tan(np.pi/4))

print(np.log(arr))

print(np.log10(arr))

print(np.subtract(v,1))

x1 = np.arange(9.0).reshape((3, 3))

print(x1)

x2 = np.arange(3.0)

print(x2)

print(np.subtract(x1,x2))

print(np.add([1,5,9],x1))

print(np.multiply(v,2))

print(np.divide(v,2))

print(np.power(v,2))

print(np.absolute(v-3))

i = np.array([1,1,2,2,3,3,3,3])

print(i)

print(np.mean(v))

print(np.median(v))

# print(x1.carrcoef())