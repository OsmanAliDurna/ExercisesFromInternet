import numpy as np
import pandas as pd

ser = pd.Series([10,88,3,4,5])

print(ser)

print(ser.size)

print(ser.ndim)

print(ser.values)

print(ser.head(2))

print(ser.tail(3))

labels = {"a","b","c"}

my_list = [10,20,30]

arr = np.array([40,50,60])

d = {"a":10,"b":20,"c":30}

dict_series = pd.Series(data = my_list)

print(pd.Series(data = my_list))

print(pd.Series(data = my_list, index = labels))

print(pd.Series(arr,labels))

print(pd.Series(d))

print(pd.Series(d,["a","c","x"]))

labels2 = ["a","b","c"]

print(pd.Series(data = labels2))

ser1 = pd.Series([1,2,3,4], index = ['USA', 'Germany','USSR', 'Japan'])

ser2 = pd.Series([1,2,5,4], index = ['USA', 'Germany','Italy', 'Japan'])

print(ser1)

print(ser2)

print(ser1[0])

print(ser1["Japan"])

print(ser1+ser2)

a = np.array([1,22,333,4444,75])

panser = pd.Series(a)

print(panser[:3])

panser = pd.Series([121, 200, 150, 99],
                  index = ["martin", "joseph", "orion", "jason"])

print(panser["martin"])

print(panser["joseph":"jason"])

print(panser.index)

print(panser.keys())

print(panser.values)

print(panser.items())

print(list(panser.items()))

for index,value in panser.items():
    print(index, " - ", value)

print("Jack" in panser)

print("martin" in panser)

print(121 in panser.values)

print(panser)

print(panser>100)

print(panser.drop("jason", inplace= True))