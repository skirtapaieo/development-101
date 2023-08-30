# machinelearning-101

This is based on the problems in Algoexperts Machine Experts training. 

The "problem" with those exercises is that they are designed to pass coding interviews. 

The solutions that are passing could be seen as "MVP's", that might be optimized in many ways before reaching production. 

I try to optimize the solutions a bit, but a lot of the issues in reality is related to data quality. 

## Index

- [1 Math Concepts](#1-math-concepts)
  - [1.1 Sparse Matrix Multiplication](#11-sparse-matrix-multiplication)
  - [1.2 Get Statistics](#12-get-statistics)

- [2 Model Concepts](#2-model-concepts)
  - [K Nearest Neighbors](#k-nearest-neighbors)



# 1 Math Concepts 

## 1.1 Sparse Matrix Multiplication

### The Problem 

Write a function that takes two integer matrices and multiplies them together. 

Both matrices will be sparse, meaning that most of their elements will be zero. 

Take advantage of that to reduce the  number of total computations that your function performs.

If the matrices can't be multiplied together, your function should return [[]]. 

<code>
matrix_a = [
    [0, 2, 0], 
    [0, -3, 5],
]
matrix_b =  [
   [0, 10, 0],
   [0, 0, 0],
   [0, 0, 4],
]
print(sparse_matrix_multiply(matrix_a, matrix_b))
</code>

### The solution 

See sparse-matrix-multiplication.py

### Why it matters? 

A sparse matrix is a matrix in which most of the elements are zero. 

The opposite of a sparse matrix is a dense matrix, where most of the elements are non-zero. 

Sparse matrices appear in many real-world situations, including:

- In social networks, where a matrix might represent connections between people. Most people are connected to only a small fraction of all other people, so the adjacency matrix is sparse.
- In text data, where a matrix might represent word frequencies in documents. Most words only appear in a small fraction of documents, so the document-term matrix is sparse.
- In scientific computing, when solving partial differential equations over a three-dimensional domain, the matrix that represents the domain is usually sparse.

Sparse matrices are important because storing and manipulating them in a naive way can be very inefficient. For example, if you store a sparse matrix as a standard two-dimensional array, you'll waste a lot of space storing zeros. 

Similarly, if you perform operations on a sparse matrix as though it were dense, you'll waste a lot of time multiplying by and adding zeros. This is why special data structures and algorithms for sparse matrices have been developed.

## 1.2 Get Statistics 

### The Problem  

Write a function that takes in a list of numbers and returns a dictionary.  

<code>input_list = [2,1,3,4,4,5,6,7]</code>

The dictionary should have statistics about: 

- the mean, 
- median, 
- mode, 
- sample variance,
- sample standard deviation, 
- and 95% confidence interval for the mean.

A sample output: 

<code>{
  "mean": 4.0, 
  "median": 4.0,
  "mode": 4.0,
  "sample_variance": 4.0,
  "sample_standard deviation": 2.0, 
  "mean_confidence interval": [2.6141, 5.3859],
}</code>

In addition:  
- Assume that the given list contains a large-enough number of samples from a population to use a z-score of  1.96.
- If there's more than one mode, the function can return any of them.
- No use of libraries.
- Your output values will automatically be rounded to the fourth decimal.

### The Solution 

The solution is straightforward based on the six statistics needed, there are several things that should be addee in a real-life case. 

### Solution improvement ideas 


#### Introduction 

The code in get-statistics was used at Algoexpert but there are several other things to do to make it behave in practise: 

- Error handling and logging - 
- Validation (decorator) - imported wraps
- Test cases (Algoexpert had 15 for this function)
- Performance - the mode function and the sorted list could be fixed
- Memory usage - when the list is long it makes sense to not have the full list in memory 
- Documentation addid docstring for Sphinx to use 
- Code style - PEP8 is followed 
- Concurrency and parallelism - the computations could be made parallel using multiprocessing 

#### Modified code 

```python
import logging
from functools import wraps
import unittest

logging.basicConfig(level=logging.INFO)

def validate_input(func):
    @wraps(func)
    def wrapper(data):
        if not isinstance(data, (list, tuple)):
            logging.error("Input should be of type list or tuple.")
            raise TypeError("Input should be of type list or tuple.")
        if len(data) == 0:
            logging.error("Input list cannot be empty.")
            raise ValueError("Input list cannot be empty.")
        for i in data:
            if not isinstance(i, (int, float)):
                logging.error("All elements in the input list should be numbers.")
                raise ValueError("All elements in the input list should be numbers.")
        return func(data)
    return wrapper

@validate_input
def calculate_mean(data):
    return sum(data) / len(data)

@validate_input
def calculate_median(data):
    # Sorting a list can be memory-intensive for large lists
    data.sort()
    middle_index = len(data) // 2
    if len(data) % 2 == 0:
        return (data[middle_index - 1] + data[middle_index]) / 2
    else:
        return data[middle_index]

@validate_input
def calculate_mode(data):
    # This method of calculating the mode has a time complexity of O(n^2), which could be slow for large lists
    counts = {num: data.count(num) for num in data}
    return max(counts.keys(), key=lambda x: counts[x])

@validate_input
def calculate_sample_variance(data, mean):
    return sum((num - mean) ** 2 for num in data) / (len(data) - 1)

def calculate_standard_deviation(sample_variance):
    return sample_variance ** 0.5

def calculate_confidence_interval(mean, standard_deviation, sample_size):
    standard_error = standard_deviation / (sample_size ** 0.5)
    margin_of_error = 1.96 * standard_error
    return [mean - margin_of_error, mean + margin_of_error]

@validate_input
def get_statistics(input_list):
    sorted_input = sorted(input_list)
    mean = calculate_mean(sorted_input)
    median = calculate_median(sorted_input)
    mode = calculate_mode(sorted_input)
    sample_variance = calculate_sample_variance(sorted_input, mean)
    sample_standard_deviation = calculate_standard_deviation(sample_variance)
    mean_confidence_interval = calculate_confidence_interval(mean, sample_standard_deviation, len(sorted_input))
    
    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "sample_variance": sample_variance,
        "sample_standard_deviation": sample_standard_deviation,
        "mean_confidence_interval": mean_confidence_interval
    }


# Test cases
class TestStatistics(unittest.TestCase):

    def setUp(self):
        self.data = [1, 2, 3, 4, 5, 5]

    def test_mean(self):
        self.assertEqual(calculate_mean(self.data), 3.3333333333333335)

    def test_median(self):
        self.assertEqual(calculate_median(self.data), 3.5)

    def test_mode(self):
        self.assertEqual(calculate_mode(self.data), 5)

    def test_sample_variance
```

#### Multiprocessing 

Here is an example of multiprocessing. 

```python
from multiprocessing import Pool

# define your data
data = [
    [1, 2, 3, 4, 5, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15, 15]
]

# define your statistics functions, as before
def calculate_mean(data):
    return sum(data) / len(data)

def calculate_median(data):
    data.sort()
    middle_index = len(data) // 2
    if len(data) % 2 == 0:
        return (data[middle_index - 1] + data[middle_index]) / 2
    else:
        return data[middle_index]

def calculate_mode(data):
    counts = {num: data.count(num) for num in data}
    return max(counts.keys(), key=lambda x: counts[x])

def calculate_statistics(input_list):
    return {
        "mean": calculate_mean(input_list),
        "median": calculate_median(input_list),
        "mode": calculate_mode(input_list),
    }

# define a function to process each list
def process_list(input_list):
    return calculate_statistics(input_list)

# create a multiprocessing Pool
with Pool() as pool:
    results = pool.map(process_list, data)

# print the results
for i, result in enumerate(results):
    print(f"Statistics for list {i+1}: {result}")

```


# 2 Model Concepts 

## K Nearest Neighbors


