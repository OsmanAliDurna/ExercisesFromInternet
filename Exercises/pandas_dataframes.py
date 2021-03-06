from os import sep
import numpy as np
import pandas as pd

datam = [10,20,30,40,50]

print(pd.DataFrame(datam, columns=["column_name"]))

m = np.arange(1,10).reshape((3,3))

print(pd.DataFrame(m, columns=["var1","var2","var3"]))

df = pd.DataFrame(data = m, columns=["var1","var2","var3"])

print(df, df.head(2), df.tail(2), df.columns, sep = "\n")

df.columns = ["new1","new2","new3"]

print(df)

print(df.shape)

print(df.size, df.ndim, df.values, sep = "\n")

s1 = np.random.randint(10, size = 5)
s2 = np.random.randint(10, size = 5)
s3 = np.random.randint(10, size = 5)

myDict = {"var1" : s1, "var2" : s2, "var3" : s3}

df1 = pd.DataFrame(myDict)

print(df1)