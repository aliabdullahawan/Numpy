import numpy as np

data = np.array([[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10]])
print(data)

data_sum = np.sum(data)
print(data_sum)
data_mean = np.mean(data)
print(data_mean)
data_std = np.std(data)
print(data_std)
data_var = np.var(data)
print(data_var)
data_min = np.min(data)
print(data_min)
data_max = np.max(data)
print(data_max)
data_argMin = np.argmin(data)
print(data_argMin)
data_argMax = np.argmax(data)
print(data_argMax)
data_avg = np.average(data)
print(data_avg)

data_summOFColumns = np.sum(data, axis=0)
print(data_summOFColumns)
data_SumOfRows = np.sum(data, axis=1)
priint(data_SumOfRows)


