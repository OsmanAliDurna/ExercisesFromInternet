import numpy as np
import pandas as pd
from pandas.core.series import Series

myindex = ['USA', 'Canada', 'Mexico']
mydata = [1776, 1867, 1821]
myser = pd.Series(data=mydata)

print(myser)

print(type(myser))

print(pd.Series(data=mydata, index=myindex))

print(myser[0])

ages = {'Sam': 5, 'Frank': 10, 'Spike': 7}

print(pd.Series(ages))

q1 = {'Japan': 80, 'China': 450, 'India': 200, 'USA': 250}
q2 = {'Brazil': 100, 'China': 500, 'India': 210, 'USA': 260}

sales_q1 = pd.Series(q1)
sales_q2 = pd.Series(q2)

print(sales_q1['Japan'])

print(sales_q2[0])

print(sales_q1.keys())

print(sales_q1+sales_q2)

print(sales_q1.add(sales_q2, fill_value=0))

np.random.seed(101)
mydata = np.random.randint(0,101,(4,3))

print(mydata)

myindex = ['CA', 'NY', 'AZ', 'TX']

mycolumns = ['Jan', 'Feb', 'Mar']

df = pd.DataFrame(mydata)

print(df)

df = pd.DataFrame(mydata, myindex, mycolumns)

print(df)

print(df.info())

print(df.head(1))

print(df.tail(1))

print(df.describe())

print(df.describe().transpose)

print(df[['Jan','Mar']])

df['Total'] = df['Jan'] + df['Feb'] + df['Mar']

print(df)

print(df.drop('Feb', axis=1))                   # for delete columns for view

print(df.drop('AZ'))                            # for delete rows for view

print(df.drop('Total', axis=1, inplace=True))   # for delete forever

print(df.index)

print(df.set_index("Feb"))

print(df.set_index("Feb").reset_index())

print(df.iloc[0:2])

print(df.loc[['AZ','CA']])