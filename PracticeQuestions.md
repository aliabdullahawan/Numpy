1. Border of ones
   Create a 10×10 array that has 1 on the border and 0 inside.

2. Modify central block
   Make a 6×6 matrix of zeros and then change its central 2×2 block to ones.

3. Row-values matrix
   Without loops or tile, create a 5×5 matrix where each row contains the values 0,1,2,3,4 (i.e., every row is [0, 1, 2, 3, 4]).

4. Replace high values
   Generate an array of 20 random integers between 1 and 100. Replace all elements greater than 50 with -1, without changing the original shape.

5. Normalise a 2D array
   Create a 5×5 array of random floats between 0 and 100. Normalise it so that all values lie in the range [0, 1]. (Use min-max scaling.)

6. Common elements
   Given two 1D arrays a = np.array([1,2,3,2,3,4,3,4,5,6]) and b = np.array([7,2,10,2,7,4,9,4,9,8]), find all elements that appear in both arrays (unique common values).

7. Remove elements present in another array
   From a = np.array([1,2,3,4,5,6,7,8,9]) remove all elements that are present in b = np.array([2,4,6,8]). Return the result as a new sorted array.

8. Positions of matches
   For a = np.array([5,7,9,2,4]) and b = np.array([1,2,3,4,5,6,7,8,9]), find the indices in b where the elements of a occur. (Assume all elements of a appear in b.)

9. Euclidean distances between vectors (broadcasting)
   Given matrix X of shape (50, 3) and matrix Y of shape (20, 3), compute the Euclidean distance between every row of X and every row of Y. Result should be a (50, 20) matrix. No loops.

10. Max value index per row
    Given a 2D array arr of shape (10, 5), return a 1D array containing the column index of the maximum value for each row.

11. Replace odd numbers
    From an array of 20 random integers between 0 and 100, replace all odd numbers with -1 without affecting even numbers.

12. Stack arrays
    Create two 3×3 arrays: A filled with 1s and B filled with 2s. Stack them:

Vertically (to get a 6×3 array)

Horizontally (to get a 3×6 array)

13. Split an array
    Take a 1D array of 30 consecutive integers (0-29). Split it into 6 equally sized contiguous sub-arrays. Then split a 6×6 array of these numbers (reshape first) into two equal parts along the column axis.

14. Column statistics
    Generate a 10×4 random matrix with values from a standard normal distribution. Compute the mean, median, and standard deviation for each column.

15. Most frequent value
    Given the array arr = np.random.randint(0, 10, 100), find the most frequent value(s). (If there’s a tie, return all values with the highest count.)

16. Simple linear regression (normal equation)
    You have data: X = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([1.2, 1.4, 1.6, 2.0, 2.1, 2.2]). Fit a linear model y = w0 + w1\*x using the normal equation:
    W = (XᵀX)⁻¹ Xᵀ y. (Don’t forget the intercept term – add a column of ones.)

17. Mean filter on an image
    A grayscale image is represented as a 2D array img of shape (100, 100). Apply a 3×3 uniform smoothing filter (box blur) without loops. Use slicing to replace each pixel (except the border) by the mean of its 3×3 neighbourhood. You can leave the border unchanged.

18. Pairwise distance matrix
    Given a set of points as a 2D array pts of shape (N, 2), compute the N×N pairwise Euclidean distance matrix using broadcasting and vectorisation, without loops.

19. Checkerboard pattern
    Write a function that takes n and returns an n×n array with a checkerboard pattern of 0s and 1s (top-left element is 1).

20. Moving average
    Given a 1D array data and a window size k, compute the moving average sequence using np.convolve (or np.cumsum). The output length should be len(data) - k + 1, containing the averages of every contiguous window of size k.

21. Sort and append
    Create a 4×4 random integer array, sort it along the columns, then append one extra row and one extra column.

22. Unique and membership checks
    Given a 1D array with repeated values, return the unique values and a boolean mask showing which elements belong to a second array.

23. Expand dimensions
    Take a 2D array and expand it once along axis 0 and once along axis 1. Describe the resulting shapes.

24. Percentiles and histogram
    Generate a random matrix and compute the 25th, 50th, and 75th percentiles, then build a histogram with custom bin edges.

25. Correlation and covariance
    For a 2D array where each column is a variable, compute the correlation matrix and covariance matrix.

26. Flip, clip, and delete
    Take a sample array, flip it left-to-right, clip its values to a range, and delete selected positions.

27. Set operations
    Given two 1D arrays, compute their union, intersection, difference, symmetric difference, and membership mask.
