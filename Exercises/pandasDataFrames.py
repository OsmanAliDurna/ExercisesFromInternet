import numpy as np
import pandas as pd

df3 = pd.DataFrame(np.random.randn(5,4), index='A B C D E'.split(), columns="W X Y Z".split() )

print(df3)

print(df3['W'], df3[['W']], type(df3['W']), type(df3[['W', 'Z']]), sep='\n')

print(df3["A":"A"])

print(df3["A":"C"])

df3["new"] = df3["W"] + df3["Y"]

print(df3)

print(df3.drop("new", axis=1)) # inplace=True sadece göstermede değil asıl datayıda güncelliyor.

m = np.random.randint(1,30,size=(10,3))

df4 = pd.DataFrame(m, columns= ["var1", "var2", "var3"])

print(df4.loc[1])

print(df4.loc[1:4])

print(df4.iloc[1:4])

df4.index ="a b c d e f g h i j".split()

print(df4)

print(df4.iloc[1:4])

# print(df4.loc[1:4]) => 1 veya 4 index isimleri yok

print(df4.loc["a":"d"])

print(df3>0)

print(df3[df3>0])

print(df3[df3["W"]>0]) # W sütununda şartı sağlayan değerleri getirdi ancak diğer satırların içeriğinin şartı sağlaması gerekmedi

print(df3[df3["W"]>0]["Y"]) # seri olarak döndü

print(df3[df3["W"]>0][["Y", "X"]]) # dataframe olarak döndü

print(df3[(df3["W"]>0) & (df3["Y"]>0)])

print(df3.loc[(df3.X>0), ["X", "Z"]])

df = pd.read_csv("tips.csv")

print(df.head())

print(df["total_bill"]>30)

print(df[df["sex"] == "Female"])

