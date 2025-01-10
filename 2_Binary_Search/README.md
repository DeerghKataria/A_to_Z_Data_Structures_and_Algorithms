# Binary Search Implementation

## Introduction

Binary search is an efficient algorithm used to find the position of a target element in a sorted list. Unlike linear search, which checks each element sequentially, binary search divides the search range in half at each step, significantly reducing the number of comparisons.

### Prerequisite
- **The array must be sorted** before applying binary search. This is a fundamental requirement for the algorithm to work correctly.

### Time Complexity
- **Best case**: \(O(1)\) (when the element is found in the middle on the first try).
- **Worst case**: \(O(\log n)\) (when the search space is repeatedly halved).
- **Average case**: \(O(\log n)\).

---

## Overview of the Code

This Python script implements binary search to locate a target element in a sorted list.

### How It Works:
1. **Preprocessing**:
   - The input array is sorted before applying the binary search algorithm.

2. **Function**:
   - The function `binarySearchAlgo` accepts two arguments:
     - `arr`: A sorted list of integers.
     - `target`: The integer value to search for.
   - It initializes pointers (`low` and `high`) to define the search range.
   - It calculates the midpoint (`mid`) of the current range and compares the target value with the middle element:
     - If the middle element matches the target, its index is returned.
     - If the target is smaller, the search range is adjusted to the left half.
     - If the target is larger, the search range is adjusted to the right half.
   - If the search range is exhausted, the function returns `-1`.

3. **User Input**:
   - The user is prompted to enter a target value.
   - The result is displayed, indicating whether the element was found and its index.

---

## Running the Code

1. Copy the script into a Python file or an IDE.
2. Ensure the input array is initialized in the `array` variable.
3. Run the script and enter a target value when prompted.

