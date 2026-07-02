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

data_sin = np.sin(data)
print(data_sin)
data_cos = np.cos(data)
print(data_cos)
data_tan = np.tan(data)
print(data_tan)
data_log = np.log(data)
print(data_log)
data_log10 = np.log10(data)
print(data_log10)
data_log2 = np.log2(data)
print(data_log2)
data_exp = np.exp(data)
print(data_exp)


print(np.pi)

data_area = np.pi * (data ** 2)
print(data_area)

data_curcumfarance = 2 * np.pi * data
print(data_curcumfarance)

