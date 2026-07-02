import numpy as np 

data1 = np.array([[1, 2, 3, 4]])
print((data1))

data2 = np.array([[1], [2], [3], [4]])
print(data1)

data1_shape1 = data1.shape
print(data1_shape1)

data_shape2 = data2.shape
print(data_shape2)


#    BROADCASTING EXAMPLE
# (1, 4) (4, 1) or (1, 4) (4, 4) -- yes can be broadcast becase on of each has the 1
# (2, 4) (4, 1)  -- no cannot be as of them has the 2 instead of 1 or 4(same)

dat_broadcasted = (data1 * data2)
print(dat_broadcasted)


