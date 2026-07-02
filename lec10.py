import numpy as np


data = np.arange(24).reshape(6, 4)
print(data)

# Fancy Indexing

data_fancyIndexing_rows = data[[0, 2, 4, 5], ::]
print(data_fancyIndexing_rows)

data_fancyIndexing_cols = data[::, [0, 2]]
print(data_fancyIndexing_cols)


# Boolean Indexing // Already covered in lec8.py

print(data[data > 10])
print(np.where(data > 10, data, 0))
print(data[~(data % 7 == 0)])

# -- Using numpy creating a function to calculate the sigmoid of the data array -- 
# sigmoid function -- Wee created a function to calculate the sigmoid of the data array. 
# The sigmoid function is defined as 1 / (1 + exp(-x)), where exp is the exponential function. 
# This function is commonly used in machine learning and statistics for transforming values into a range between 0 and 1.
# sigmoid = 1 / (1 + np.exp(-x))

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

data_sigmoid = sigmoid(data)
print(data_sigmoid)

# -- Mean Square Error (MSE) Calculation --
# Mean Square Error (MSE) is a common metric used to evaluate the performance of regression models. 
# It measures the average squared difference between the predicted values and the actual values. 
# A lower MSE indicates a better fit of the model to the data.
# mse = np.mean((actual - predicted) ** 2)

actual = np.random.randint(low=1, high=50, size=25)
print(actual)
predicted = np.random.randint(low=1, high=50, size=25)
print(predicted)

def mean_square_error(actual, predicted):
    return np.mean((actual - predicted) ** 2)

mse = mean_square_error(actual, predicted)
print(mse)


## -- Binary Cross Entropy (BCE) Calculation --
# Binary Cross Entropy (BCE) is a loss function commonly used in binary classification problems. 
# It measures the difference between the predicted probabilities and the actual binary labels.
# log loss = -1/n * sum(y * log(p) + (1 - y) * log(1 - p)), where n is the number of samples, y is the actual label (0 or 1), 
# and p is the predicted probability of the positive class.

def binary_cross_entropy(actual, predicted):
    epsilon = 1e-15  # Small value to avoid log(0)
    predicted = np.clip(predicted, epsilon, 1 - epsilon)  # Clip predictions to avoid log(0)
    return -np.mean(actual * np.log(predicted) + (1 - actual) * np.log(1 - predicted))

bce = binary_cross_entropy(actual, predicted)
print(bce)

# Vertical and Horizontal Stacking of Arrays
# Vertical stacking (vstack) and horizontal stacking (hstack) are methods to combine arrays in NumPy.
# Vertical stacking combines arrays along the vertical axis (rows), while horizontal stacking combines arrays along the horizontal axis (columns).

data1 = np.arange(24).reshape(6, 4)
data2 = np.arange(24, 48).reshape(6, 4)

data_vstack = np.vstack((data1, data2))
print(data_vstack)
data_hstack = np.hstack((data1, data2))
print(data_hstack)

# Vertical and Horizontal Splitting of Arrays
# Vertical splitting (vsplit) and horizontal splitting (hsplit) are methods to divide arrays
# into smaller sub-arrays in NumPy. Vertical splitting divides an array into multiple sub-arrays along the vertical axis (rows),
# while horizontal splitting divides an array into multiple sub-arrays along the horizontal axis (columns).

data1 = np.arange(24).reshape(6, 4)
data2 = np.arange(24, 48).reshape(6, 4)

data_vsplit = np.vsplit(data1, 3)
print(data_vsplit)
data_hsplit = np.hsplit(data1, 2)
print(data_hsplit)

