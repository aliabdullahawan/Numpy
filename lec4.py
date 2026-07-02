import numpy as np 

data = np.array([112.32, 139.527, 128.009, 146.805,157.172])
print(data)

data_sqrt = np.sqrt(data)
print(data_sqrt)
data_round = np.round(data)
print(data_round)
data_floor = np.floor(data)
print(data_floor)
data_ceil = np.ceil(data)
print(data_ceil)

print(np.pi)

data_area = np.pi * (data ** 2)
print(data_area)

data_curcumfarance = 2 * np.pi * data
print(data_curcumfarance)

