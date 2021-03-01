import numpy as np

my_list = [1,2,3]

print(my_list)

my_list.append(5)

print(my_list)

np_array = np.array(my_list)

print(np_array)

print( type(my_list), type(np_array), sep = "\t" )

# print(my_list*my_list2)

list_list = []

for i in range ( len(my_list) ):
    list_list.append( my_list[i] * my_list[i] )

print(list_list)

print(np_array**2)

print( np.arange(0,11,2) )

print( np.arange(10,-1,-2) )

print( np.ones(2))

print( np.zeros((3,2), dtype = bool) )

print( np.full((2,4), 3))

# C or Fortran order

print( np.full((4,4), "x", order = "C") )
print( np.full((4,4), "y", order = "F") )

print( np.linspace(0,10,51, dtype = int ))

print( np.linspace(0, 10).round(2))

print( np.eye(6))

print( np.random.rand(2,3))

print( np.random.randn(4, 4).round(2))

print( np.random.randint(0,15,4))

print( np.random.randint(15, size = ( 2, 2 )))

print( np.random.randint(0,[3,50,1000]))

print( np.random.randint(1,[3,50,1000], size = (2,3)))

print( np.random.randint([3,50,1000],[10,100,2000]))