# Linear Search Implementation

## Introduction

Linear search is a basic algorithm used to find the position(s) of a target element within a list. It works by sequentially checking each element in the list until the target element is found or the end of the list is reached.

### Time Complexity
- **Best case**: \(O(1)\) (when the element is found at the beginning).
- **Worst case**: \(O(n)\) (when the element is at the end or not present in the list).
- **Average case**: \(O(n)\).

While linear search is straightforward and effective for small datasets, it may be inefficient for larger datasets. For sorted lists, more advanced algorithms like binary search are typically used.

---

## Overview of the Code

This Python script implements a linear search to locate all occurrences of a target element in a list. 

### How It Works:
1. **Function**:
   - The function `linearSearch` accepts two arguments:
     - `arr`: A list of integers.
     - `target`: The integer value to search for.
   - It iterates through the list and appends the index of each occurrence of the target element to a result list.
   - The function returns the list of indices where the target is found.

2. **Sample Usage**:
   - A predefined list of integers (`array`) is searched for a target value (`4`).
   - The indices of all occurrences are printed.
   - If the target is not found, a message indicating this is displayed.

---

## Running the Code

1. Copy the script into a Python file or an IDE.
2. Adjust the `array` and `target` variables as desired.
3. Run the script to observe the output.
