import numpy as np

a = np.random.rand(10,10)
max_per_row = a.max(axis=1)
min_per_row = a.min(axis=1)
Min =  a.min()
Max =  a.max()
print("Array of elements")
print(a)
print("Maximum element in each row:")
print(max_per_row)
print("Minimum element in each row:")
print(min_per_row)