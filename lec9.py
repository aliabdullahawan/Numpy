import numpy as np

rng = np.random.default_rng() # np.random.default_rng(seed=1) -- also can use that (It ensures that other developers running your code get the same results.)
print(rng)

random_int = rng.integers(low=1, high=7, size=(3, 2))    # siz=6 - 1D  size=(2, 3) - 3D
print(random_int)

random_float_0to1 = rng.random(size=(3, 2))  # Floating between 0 to 1
print(random_float_0to1)

random_float = rng.uniform(low=10, high=20, size=5)  # Floating betweeen low to high
print(random_float)


colors = np.array(["Red", "Blue", "Green", "Yellow", "Teal", "Purple"])
choice = rng.choice(colors)
print(choice)
choices = rng.choice(colors, size=5)
print(choices)
choices = rng.choice(colors, size=(2, 3))
print(choices)
choices = rng.choice(colors, size=3, replace=False)
print(choices)

shuffe = np.array([1, 2, 3, 4, 5])  # Shuffles an existing array
rng.shuffle(shuffe)
print(shuffe)

arr = np.array([1, 2, 3, 4, 5])  # Returns a shuffled copy instead of modifying the original
new_arr = rng.permutation(arr)
print(arr)
print(new_arr)

arr = rng.binomial(n=10, p=0.5, size=5)   # Binomial Distribution
print(arr)

arr = rng.poisson(lam=5, size=5)  # Poisson Distribution
print(arr)

arr = rng.exponential(scale=2, size=5)  # Exponential Distribution
print(arr)

arr = rng.standard_normal(size=5)  # Shortcut for a normal distribution with mean = 0 and std = 1.
print(arr)

b = rng.bytes(10)  # Generate random bytes.
print(b)

arr = rng.normal(loc=0, scale=1, size=5)  # Normal (Gaussian) Distribution
print(arr)