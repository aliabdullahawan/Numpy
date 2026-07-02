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

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

data_sigmoid = sigmoid(data)
print(data_sigmoid)

# -- Mean Square Error (MSE) Calculation --
# Mean Square Error (MSE) is a common metric used to evaluate the performance of regression models. 
# It measures the average squared difference between the predicted values and the actual values. 
# A lower MSE indicates a better fit of the model to the data.

actual = np.random.randint(satrt=1, stop=50, size=25)
print(actual)
predicted = np.random.randint(satrt=1, stop=50, size=25)
print(predicted)

def mean_square_error(actual, predicted):
    return np.mean((actual - predicted) ** 2)

mse = mean_square_error(actual, predicted)
print(mse)





