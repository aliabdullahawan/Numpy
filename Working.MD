# NumPy Study Hub

This folder is a compact NumPy learning path. The lecture files build from basic array creation to slicing, vectorized math, broadcasting, statistics, filtering, random data, array manipulation tricks, and small machine-learning style helpers.

## Start Here

1. Read the lecture files in order from `lec1.py` to `lec10.py`.
2. Run each script so you can see the printed results.
3. Rework the examples by hand to make the concepts stick.
4. Use `PracticeQuestions.md` after a few lessons to test yourself.
5. Open the cheat-sheet PDFs when you want a quick syntax reference.

## What Each Lecture Covers

| File        | Main Topic                                                                                                                                                                                     |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `lec1.py`   | NumPy basics, version check, arrays, `dtype`, `shape`, `ndim`, reshaping, and indexing into 3D data.                                                                                           |
| `lec2.py`   | Slicing and subscript-based selection across rows and columns.                                                                                                                                 |
| `lec3.py`   | Elementwise arithmetic on arrays.                                                                                                                                                              |
| `lec4.py`   | Mathematical functions like `sqrt`, `round`, `floor`, `ceil`, trig, logs, `exp`, and using `pi`.                                                                                               |
| `lec5.py`   | Elementwise operations, comparisons, and in-place masking with boolean conditions.                                                                                                             |
| `lec6.py`   | Broadcasting rules and how NumPy combines arrays of compatible shapes.                                                                                                                         |
| `lec7.py`   | Reductions and summary statistics such as `sum`, `mean`, `median`, `std`, `var`, `min`, `max`, `argmin`, `argmax`, and axis-based aggregation.                                                 |
| `lec8.py`   | Filtering, boolean indexing, `np.where`, even/odd checks, logical negation, and handling missing values with `NaN`.                                                                            |
| `lec9.py`   | Random number generation with `default_rng`, random integers/floats, sampling, shuffling, permutations, and common distributions.                                                              |
| `lec10.py`  | Fancy indexing, boolean filtering recap, sigmoid, mean squared error, binary cross entropy, stacking, and splitting.                                                                           |
| `tricks.py` | Sorting, appending, concatenation, uniqueness, dimension expansion, cumulative sums, percentiles, histograms, correlation, covariance, membership checks, flips, clipping, and set operations. |

## Core Ideas In One Place

### 1) Array Foundations

NumPy revolves around ndarrays. The most important early ideas are:

- creating arrays from lists or ranges
- understanding `shape`, `ndim`, and `dtype`
- reshaping and reading data by index

### 2) Indexing And Slicing

You use slicing to pull out rows, columns, and subarrays without loops. The lesson files show:

- normal slicing with start, stop, and step
- reverse slicing
- selecting row and column patterns
- fancy indexing with index lists

### 3) Vectorized Math

NumPy is powerful because operations run on whole arrays at once:

- arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- comparisons: `==`, `!=`, `<`, `<=`, `>`, `>=`
- universal functions: `sqrt`, `round`, `floor`, `ceil`, `sin`, `cos`, `tan`, `log`, `log10`, `log2`, `exp`

### 4) Broadcasting

Broadcasting lets NumPy combine arrays of different but compatible shapes. The key rule is simple: dimensions must match or one of them must be `1`.

### 5) Statistics And Reduction

The lecture set covers the summary operations you use constantly in data work:

- totals and averages
- medians and variation
- minimums, maximums, and their positions
- computing column-wise or row-wise values with `axis`

### 6) Filtering And Missing Data

The filtering lesson shows the main patterns for real data:

- boolean masks
- `np.where`
- selecting even or odd values
- removing unwanted elements
- handling missing values with `np.nan`

### 7) Random Data

Random generation is useful for testing, simulation, and exercises. The examples cover:

- integers, floats, uniform values, and sampling
- shuffle versus permutation
- distributions such as binomial, poisson, exponential, standard normal, and normal

### 8) Vectorized Helpers For ML-Style Work

The final lecture uses NumPy to build reusable numeric helpers such as:

- sigmoid
- mean squared error
- binary cross entropy

### 9) Array Tricks And Utility Patterns

The new tricks file collects common NumPy patterns that are easy to reuse in exercises and data work:

- sorting and appending
- concatenating and stacking arrays
- unique values and set-style operations
- expanding dimensions and cumulative sums
- percentiles, histograms, correlation, and covariance
- membership checks, flips, `put`, `delete`, and clipping

## Practice Question Themes

The practice sheet is organized around the same NumPy skills, but in problem form.

### Array Construction And Manipulation

- border arrays
- central blocks
- repeated row patterns
- stacking and splitting arrays
- checkerboard patterns

### Masking And Filtering

- replacing values above or below a threshold
- removing odd numbers
- finding common values
- removing values from one array using another

### Broadcasting And Distances

- Euclidean distances between vectors
- pairwise distance matrices
- row-wise and column-wise operations without loops

### Statistics And Frequency

- column statistics
- most frequent value
- max index per row
- moving averages

### Applied NumPy

- min-max normalization
- linear regression with the normal equation
- mean filtering on an image
- sigmoid and loss-style calculations

### Array Tricks And Reshaping

- sorting, stacking, and splitting arrays
- unique values and set operations
- expanding dimensions for model inputs
- cumulative sums and clipping values
- histogram and summary-style exploration

## Cheat-Sheet References

The PDF files in this folder are quick-reference NumPy cheat sheets. They reinforce the same core material used throughout the lectures:

- importing NumPy as `np`
- creating arrays with `array`, `zeros`, `ones`, `empty`, `arange`, and `linspace`
- loading and saving data with `loadtxt`, `genfromtxt`, and `savetxt`
- everyday array operations, indexing, reshaping, and manipulation patterns

## Study Workflow

If you want the fastest progress, use this loop:

1. Read one lecture file.
2. Run it.
3. Predict the output before you look.
4. Change the numbers and rerun.
5. Solve a few practice questions from the matching topic.
6. Review the cheat-sheet PDFs when you need a syntax reminder.

## Quick Reminders

- Prefer vectorized NumPy operations instead of Python loops when possible.
- Use boolean indexing for clean filtering.
- Use `np.nan` for missing numeric values.
- Use `&`, `|`, and `~` for array conditions instead of `and`, `or`, and `not`.
- Broadcasting is one of the most important NumPy ideas to understand early.

## Current Focus

The current focus is `lec10.py` and `tricks.py`, which extend the course into fancy indexing, stacking and splitting, and a broader set of reusable NumPy utilities.
