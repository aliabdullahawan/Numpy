import numpy as np

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],
                 [10, 11, 12], [13, 14, 15]])
#print(data)

data_slices_subscript = data[::-2]
#print(data_slices_subscript)

data_subscriping_rowSelection = data[::-1, 0::2]
#print(data_subscriping_rowSelection)



