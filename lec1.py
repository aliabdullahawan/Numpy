import numpy as np


print(np.__version__)

data = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                 [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
                 [[21, 22, 23], [24, 25 ,26], [27, 28, 29]]])
print(data)

data = np.arange(24).reshape(6, 4)
print(data)

data_type = data.dtype
print(data_type)

datax5 = data * 5
print(datax5)

data_dim = np.ndim(data)
print(data_dim)

data_shap = data.shape
print(data_shap)

print(data[2, 1, 0])

