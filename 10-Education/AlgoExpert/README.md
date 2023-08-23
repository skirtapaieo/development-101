# Algoexpert

## Exercises

- Arrays
- Binary Search Trees
- Binary Trees
- Dynamic Programming
- Famous Algorithms
- Graphs
- Greedy Algorithms
- Heaps
- Linked Lists
- Recursion
- Searching
- Sorting
- Stacks
- Strings
- Tries

# Arrays

## Outline

- [Tournament Winner](#tournament-winner)
- [Sorted Squared Arrays](#sorted-squared-arrays)
- [Validate Subsequence](#validate-subsequence)
- [Apartment Hunding](#apartment-hunting)

# Tournament Winner

## Outline

- [Tournament Winner](#tournament-winner)
  - [1 Objective](#1-objective)
    - [1.1 Description](#11-description)
    - [1.2 Sample Input](#12-sample-input)
    - [1.3 Sample Output](#13-sample-output)
    - [1.4 Test Cases](#14-test-cases)
    - [1.6 Non-functional Requirements](#16-non-functional-requirements)
  - [Conceptual Understanding](#conceptual-understanding)
  - [Solution Approaches](#solution-approaches)
    - [Brute Force](#brute-force)
      - [Brute Force Complexity](#brute-force-complexity)
    - [Optimized Approach with HashMap](#optimized-approach-with-hashmap)
      - [HashMap Complexity](#hashmap-complexity)
  - [Language for Prototype and for Optimization](#language-for-prototype-and-for-optimization)

## 1 Objective

### 1.1 Description

There's an algorithms tournament taking place in which teams of programmers compete against each other to solve algorithmic problems as fast as possible.

- Teams compete in a round robin, where each team faces off against all other teams.
- Only two teams compete against each other at a time,
- and for each competition, one team is designated the home team, while the other team is the away team.
- In each competition there's always one winner and one loser; there are no ties.
- A team receives 3 points if it wins and 0 points if it loses.
- the winner of the tournament is the team that receives the most amount of points.

Given an array of pairs representing the teams that have competed against each other and an array containing the results of each competition, write a function that returns the winner of the tournament. The input arrays are named competitions and results, respectively.

The competitions array has elements in the form of [homeTeam, awayTeam], where each team is a string of at most 30 characters representing
the name of the team.

The results array contains information about the winner of each corresponding competition in the competitions array.

Specifically, results[i] denotes the winner of competitions[i], where a 1 in the results array means that the home team in the corresponding competition won and a means that the away team won.

It's guaranteed that exactly one team will win the tournament and that each team will compete against all other teams exactly once. It's also
guaranteed that the tournament will always have at least two teams.

### 1.2 Sample input

### 1.3 Sample output

### 1.4 Test cases

### 1.6 Non-functional requirements

1000 teams, 10,000 programmers

## Conceptual understanding

To solve the given problem, we need to determine the team that has the highest number of points in the tournament. We can approach this problem in multiple ways, each with different time and space complexities. Here are a few possible approaches:

## Solution Approaches

### Brute Force

One simple approach is to iterate over the competitions array and update the points for each team based on the results array. After processing all the competitions, we can find the team with the maximum points and return it as the winner.

#### Brute Force Complexity

This approach has a time complexity of O(n^2), where n is the number of teams.

### Optimized approach with HashMap

Instead of updating the points for each team during iteration, we can use a dictionary (HashMap) to store the points for each team.

#### Hashmap complexity

This approach has a time complexity of O(n), where n is the number of competitions.

### Language for prototype and for optimization

We picked Python in this case, to elaborate the approaches, but we will also test to optimize it, in Python and C++.

| Rank | Language   | Key Characteristics                                                                                           |
| ---- | ---------- | ------------------------------------------------------------------------------------------------------------- |
| 1    | C++        | High performance, efficient memory management, widely used for competitive programming and system-level tasks |
| 2    | Java       | Strong ecosystem, extensive libraries, good performance characteristics                                       |
| 3    | Python     | Simplicity, readability, large standard library, rapid development                                            |
| 4    | Go         | Concurrency, efficient execution, scalability                                                                 |
| 5    | C#         | Integration with Windows development, wide range of libraries and tools                                       |
| 6    | JavaScript | Primarily used for web development, wide browser support                                                      |
| 7    | TypeScript | Static typing, improved tooling, maintainability                                                              |
| 8    | Swift      | Apple platform development, modern syntax, strong type safety                                                 |

# Sorted squared array

## Outline

- [Sorted Squared Array](#sorted-squared-array)
  - [Objective](#objective)
  - [Approaches](#approaches)
    - [Naive Approach (and its complexity)](#naive-approach-and-its-complexity)
    - [Two Pointers Approach](#two-pointers-approach)
    - [Using a Double-Ended Queue](#using-a-double-ended-queue)

## Objective

We need to understand the problem of a sorted squared array.

We want to look at different solutions, in terms of time and space complexity. We will use Pyhon to implement in this case.

We need to a function that

- takes in a non-empty array of integers
- that are sorted in ascending order and
- returns a new array of the same length
- with the squares of the original integers
- also sorted in ascending order.

## Approaches

### Naive Approach (and its complexity)

We square each element in the array, sort the array, and return it.

This approach requires no extra space (other than the output array), so the space complexity is O(n). However, because Python's built-in sort function has a time complexity of O(n log n), the time complexity for this solution is also O(n log n).

````python
def sorted_squared_array(array):
    return sorted([i**2 for i in array])
´´´

### Two pointers approach

This approach is based on the fact that the input array is already sorted. Since it's sorted but we're squaring, the largest numbers could be at the beginning or end of the array (due to negative numbers).

We can use two pointers, one at the start of the array and one at the end, and compare the squares of the elements at these pointers. We fill our result array from the end and move our pointers accordingly.

This approach has a time complexity of O(n) as we are visiting each element exactly once. The space complexity is also O(n) as we are creating a new array to store the result.

```python
def sorted_squared_array(array):
    n = len(array)
    result = [0] * n
    start, end = 0, n - 1

    for i in range(n - 1, -1, -1):
        if abs(array[start]) > abs(array[end]):
            result[i] = array[start] ** 2
            start += 1
        else:
            result[i] = array[end] ** 2
            end -= 1

    return result

````

### Using a double-ended queue

This approach is similar to the two pointers approach, but instead of using an array for the result, we use a deque (double-ended queue). We append to the front of the deque, which can be done in O(1) time, the larger of the two squares at the start and end of the array. This approach has the same time and space complexities as the two pointers approach: O(n).

```python
from collections import deque

def sorted_squared_array(array):
    n = len(array)
    result = deque()
    start, end = 0, n - 1

    for _ in range(n):
        if abs(array[start]) > abs(array[end]):
            result.appendleft(array[start] ** 2)
            start += 1
        else:
            result.appendleft(array[end] ** 2)
            end -= 1

    return list(result)

```

# Validate Subsequence

## Outline

- [Validate Subsequence](#validate-subsequence)
  - [Objective](#objective)
  - [Conceptual View](#conceptual-view)
    - [Iterative Approach](#iterative-approach)
      - [Complexity of Iterative Solution](#complexity-of-iterative-solution)
    - [Optimization using Python's Built-in Functions](#optimization-using-pythons-built-in-functions)
    - [Recursive Approach](#recursive-approach)
      - [Complexity of Recursive Solution](#complexity-of-recursive-solution)

## Objective

Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.

- A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array.

- For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]. Note that a single number in an array and the array itself are both valid subsequences of the array.

- The function will be throughly unit tested to make sure that it is as correct as possible.

## Conceptual view

We will try a couple of approaches and also figure out the complexity of the solutions.

### Iterative approach

This approach is a two pointer approach.

- If you make it until the end of the second array (subsequence) then you have found a subsequence.
- If you make it until the end of the first array (sequence array)

```python
def isSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)
```

#### Complexity of iterative solution

Time Complexity: O(n), where n is the length of the array. This is because in the worst-case scenario we have to check each element in the array.

Space Complexity: O(1), because we're only using a constant amount of space to store our two pointers.

#### Optimization using Pythons built-in functions

This does not affect the complexity, and not really the readability, but it is using built-in functions:

```Python
def isValidSubsequence(array, sequence):
    iter_array = iter(array)
    return all(item in iter_array for item in sequence)
```

### Recursive approach

The recursive version is calls itself when two numbers are equal.

```python
def isSubsequence(array, sequence):
    return isSubHelper(array, sequence, 0, 0)

def isSubHelper(array, sequence, arrIdx, seqIdx):
    # Base cases
    if seqIdx == len(sequence):
        return True
    if arrIdx == len(array):
        return False

    # Recursive cases
    if array[arrIdx] == sequence[seqIdx]:
        return isSubHelper(array, sequence, arrIdx + 1, seqIdx + 1)
    else:
        return isSubHelper(array, sequence, arrIdx + 1, seqIdx)
```

#### Complexity of recursive solution

Time Complexity: O(n), where n is the length of the array. Just like in the iterative approach, in the worst-case scenario we have to check each element in the array.

Space Complexity: O(n) because in the worst-case scenario, we could end up with n nested recursive calls, and each call adds a level to the call stack. The call stack could be n levels deep in this case, so the space complexity is O(n).

# Apartment Hunting

Algorithm for picking a proper apartment block, based on a few requirements (from exercise on AlgoExpert.io)

# Outline

- [The Objective](#the-objective)
- [Conceptual view](#conceptual-view)
- [Approach](#approach)
- [Solution](#solution)
- [Time and Space Complexity](#time-and-space-complexity)
- [Testing](#testing)
- [Conclusions](#conclusions)

## The Objective

You're looking to move into a new apartment on specific street, and you're given a list of contiguous blocks on that street where each block
contains an apartment that you could move into.

You have a list of requirements:

- a list of buildings that are important to you. You might value having a school and a gym near your apartment.
- The list of blocks that you have contains information at every block about all of the buildings that are present/absent at the block in
  question. For every block, you might know whether a school, a pool, an office, and a gym are present.

In order to optimize your life, you want to pick an apartment block such that you minimize the farthest distance you'd have to walk from your
apartment to reach any of your required buildings.

Write a function that takes in a list of contiguous blocks on a specific street and a list of your required buildings and that returns the location (the index) of the block that's most optimal for you.

If there are multiple most optimal blocks, your function can return the index of any one of them.

```
blocks = [
  {
   "gym": false,
   "school": true,
   "store": false,
  },
 {
   "gym": true,
   "school": false,
   "store": false,
  },
 {
   "gym": true,
   "school": true,
   "store": false,
     },
    {
   "gym": false,
   "school": true,
   "store": false,
  },
 {
   "gym": false,
   "school": true,
   "store": true,
  },
]
reqs = ["gym", "school", "store"]
```

## Conceptual view

We're given a list of blocks, each of which contains information about the presence or absence of certain facilities (like a gym, school, store, etc.). We also have a list of personal requirements, which are the facilities that we wish to have nearby our apartment. The problem is to find the index of a block such that the farthest facility from our list of requirements is as close as possible. If multiple blocks satisfy this condition, we can return any of them.

## Approach

This problem can be solved using a variation of the dynamic programming approach. We'll start by calculating the minimum distances to each facility for each block. We'll then find the maximum of these minimum distances for each block. The block with the smallest of these maximum distances is our desired block. To calculate the minimum distances, we'll use two passes for each facility: one from left to right and one from right to left. This will ensure that we account for the closest facility in both directions.

Dynamic Programming is essentially about storing and reusing past information to make future decisions more efficient. In the problem, the application of dynamic programming lies in the way we calculate the minimum distances from a block to each requirement (facility). The idea is to break down the problem of finding the minimum distance to each facility from each block into simpler subproblems, solve those subproblems, and store their solutions to be used later.

## Solution

See apartmenthunt.py

## Time and Space complexity

The time complexity of this solution is O(b\*r), where b is the number of blocks and r is the number of requirements. This is because we perform two passes through the blocks array for each requirement.

The space complexity is O(b), because we store the minimum and maximum distances for each block.

## Testing

Making sure to test the code with various inputs, including edge cases, to ensure it produces the expected results, is essential.

```
# Testing with provided input
blocks = [
  {
   "gym": False,
   "school": True,
   "store": False,
  },
  {
   "gym": True,
   "school": False,
   "store": False,
  },
  {
   "gym": True,
   "school": True,
   "store": False,
  },
  {
   "gym": False,
   "school": True,
   "store": False,
  },
  {
   "gym": False,
   "school": True,
   "store": True,
  },
]
reqs = ["gym", "school", "store"]

print(apartmentHunting(blocks, reqs))  # Expected: 4

# Testing when all blocks have all facilities
blocks = [
  {
   "gym": True,
   "school": True,
   "store": True,
  },
  {
   "gym": True,
   "school": True,
   "store": True,
  },
  {
   "gym": True,
   "school": True,
   "store": True,
  },
]
reqs = ["gym", "school", "store"]

print(apartmentHunting(blocks, reqs))  # Expected: 0, 1, or 2 (as all blocks are the same)

# Testing when only one block has all facilities
blocks = [
  {
   "gym": False,
   "school": False,
   "store": False,
  },
  {
   "gym": True,
   "school": True,
   "store": True,
  },
  {
   "gym": False,
   "school": False,
   "store": False,
  },
]
reqs = ["gym", "school", "store"]

print(apartmentHunting(blocks, reqs))  # Expected: 1

# Testing when no block has all facilities
blocks = [
  {
   "gym": True,
   "school": False,
   "store": False,
  },
  {
   "gym": False,
   "school": True,
   "store": False,
  },
  {
   "gym": False,
   "school": False,
   "store": True,
  },
]
reqs = ["gym", "school", "store"]

print(apartmentHunting(blocks, reqs))  # Expected: None or Error (as no block satisfies all requirements)
```

In the last test case, the implementation doesn't handle the situation when no block satisfies all requirements. It will return a block anyway. DWe should modify the code to return None or raise an error in such situations.

## Conclusions

In a real-world system design scenario, the back-end service would be responsible for executing the apartmentHunting function. The input to this function (the list of blocks and user requirements) could be provided by the front-end application where the user selects their preferences.

The front-end application could present an interactive map where blocks are highlighted based on the presence of the facilities. Once the user submits their preferences, the optimal block could be returned by the back-end service and highlighted on the map. This would provide a clear, visual, and user-friendly way to present the solution to the problem.

This design efficiently separates the computational heavy-lifting to the back-end, while keeping the front-end lightweight and responsive. It also provides a clear separation of concerns between the front-end and back-end, making the system easier to maintain and scale.
