
from time import process_time

import numpy as np

py_list = [i for i in range(10000)]

start = process_time()

py_list = [i+2 for i in py_list]

end = process_time()

print( round( end - start) )

np_arr = np.array([i for i in range(10000)])

start_np = process_time()

np_arr += 2

end_np = process_time()

print( round( end_np - start_np) )
