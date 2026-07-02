import numpy as np 

## Filtering

ages = np.array([[16, 21, 30, 45, 65, 21, 15, 19],
                 [39, 29, 99, 18, 12, 21, 20, 31]])
print(ages)

teenagesr = ages[ages <= 19]
print(teenagesr)

adults = ages[(ages >= 18 ) & (ages <= 65)] # Always use bitwise operators (&, |) instead of logical operators (and, or) when working with NumPy arrays.
print(adults)
adults = ages[(ages >= 18 ) | (ages <= 65)]
print(adults)
evens = ages[(ages % 2 == 0)]
print(evens)
print(ages[~(ages % 7 == 0)]) # For negation, use the tilde (~) operator. It is equivalent to the not operator in Python.

adults = np.where(ages >= 18, ages, 0)
print(adults)
adults = np.where(ages >= 18, ages, -1)
print(adults)
adults = np.where(ages >= 18, ages, np.nan)
print(adults)



