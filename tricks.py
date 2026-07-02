import numpy as np


data = np.random.randint(low=1, high=50, size=(6, 4))
print(data)


# We can use multiple sorted algos like quicksort, mergesort, heapsort, and stable sort to sort the data array.
# And order is the order in which the data is sorted. By default, it is None, which means that the data is sorted in ascending order.
# If axis is 0, it means that the data is sorted along the rows. If axis is 1, it means that the data is sorted along the columns.

data_sorted = np.sort(data, axis=0, kind='quicksort', order=None)
print(data_sorted)

# It will sort the data array along the rows (axis=0) using the quicksort algorithm. The sorted data will be printed.

data_appended = np.append(data, [[51, 52, 53, 54]], axis=0) # Appends a new row to the data array.
print(data_appended)

data_appended_newRow = np.append(data, [[51, 52, 53, 54]], axis=0) # Appends a new row to the data array. The new row is [51, 52, 53, 54]. The axis=0 means that the new row is appended along the rows. The new array will be printed.
print(data_appended_newRow)

data_appended_newCol = np.append(data, np.ones((data.shape[0], 1)), axis=1) # Appends a new column to the data array. The new column is filled with ones. The axis=1 means that the new column is appended along the columns. The new array will be printed.
print(data_appended_newCol)

data_appended_random = np.append(data, np.random.randint(low=1, high=50, size=(6, 4)), axis=0) # Appends a new row to the data array. The new row is filled with random integers between 1 and 50. The axis=0 means that the new row is appended along the rows. The new array will be printed.
print(data_appended_random)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

data_concatenated_rows = np.concatenate((a, b), axis=0) # Concatenates two arrays a and b along the rows (axis=0). The new array will be printed.
print(data_concatenated_rows)

data_concatenated_cols = np.concatenate((a, b), axis=1) # Concatenates two arrays a and b along the columns (axis=1). The new array will be printed.
print(data_concatenated_cols)

data_unique = np.unique(data) # Returns the unique elements of the data array. The new array will be printed.
print(data_unique)

data_expandedDim_rows = np.expand_dims(data, axis=0) # Expands the dimensions of the data array along the rows (axis=0). The new array will be printed.
print(data_expandedDim_rows)

data_expandedDim_cols = np.expand_dims(data, axis=1) # Expands the dimensions of the data array along the columns (axis=1). The new array will be printed.
print(data_expandedDim_cols)

data_cumulativeSum_rows = np.cumsum(data, axis=0) # Calculates the cumulative sum of the data array along the rows (axis=0). The new array will be printed.
print(data_cumulativeSum_rows)

data_cumulativeSum_cols = np.cumsum(data, axis=1) # Calculates the cumulative sum of the data array along the columns (axis=1). The new array will be printed.
print(data_cumulativeSum_cols)

data_percentile_100 = np.percentile(data, 100) # Calculates the 100th percentile of the data array. The 100th percentile is the maximum value in the data array. The new value will be printed.
print(data_percentile_100)

data_histogram = np.histogram(data, bins=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) # Calculates the histogram of the data array. The bins parameter specifies the bin edges. The new histogram will be printed.
print(data_histogram)

data_corelation = np.corrcoef(data, rowvar=False) # Calculates the correlation coefficient of the data array. The rowvar=False parameter specifies that the variables are represented by columns. The new correlation coefficient will be printed.
print(data_corelation)

data_covariance = np.cov(data, rowvar=True) # Calculates the covariance of the data array. The rowvar=True parameter specifies that the variables are represented by rows. The new covariance will be printed.
print(data_covariance)

data_isin = np.isin(data, [10, 20, 30]) # Checks if the elements of the data array are in the list [10, 20, 30]. The new boolean array will be printed.
print(data_isin)

data_flip_rows = np.flip(data, axis=0) # Flips the data array along the rows (axis=0). The new array will be printed.
print(data_flip_rows)

data_flip_cols = np.flip(data, axis=1) # Flips the data array along the columns (axis=1). The new array will be printed.
print(data_flip_cols)

data_flip = np.flip(data) # Flips the data array along both axes (rows and columns). The new array will be printed.
print(data_flip)

data_fliplr = np.fliplr(data) # Flips the array in the left/right direction. It reverses the order of elements in each row of the array.
print(data_fliplr)

c = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
print(c)
np.put(c, [0, 5, 10], [100, 200, 300]) # The np.put() function is used to modify specific elements of the array c.
print(c)

data_delete = np.delete(c, 0)  # 0 index is deleted from the array c. The new array will be printed.
print(data_delete)

data_clip = np.clip(data, a_min=10, a_max=30) # Clips (limits) the values in the data array to be within the range [10, 30]. Values less than 10 are set to 10, and values greater than 30 are set to 30. The new array will be printed.
print(data_clip)




# --Set Functions in numpy--
# Set functions in NumPy are used to perform operations on arrays that involve unique elements, intersections

data_set1 = np.array([1, 2, 3, 4, 5])
data_set2 = np.array([4, 5, 6, 7, 8])

data_union = np.union1d(data_set1, data_set2) # Returns the unique elements that are present in either of the two input arrays. The new array will be printed.
print(data_union)

data_intersection = np.intersect1d(data_set1, data_set2) # Returns the unique elements that are present in both of the two input arrays. The new array will be printed.
print(data_intersection)

data_difference = np.setdiff1d(data_set1, data_set2) # Returns the unique elements that are present in the first input array but not in the second input array. The new array will be printed.
print(data_difference)

data_symmetric_difference = np.setxor1d(data_set1, data_set2) # Returns the unique elements that are present in either of the two input arrays but not in both. The new array will be printed.
print(data_symmetric_difference)


data_in1d = np.in1d(data_set1, data_set2) # Returns a boolean array indicating whether each element of the first input array is present in the second input array. The new boolean array will be printed.
print(data_in1d)






