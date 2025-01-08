# The pre-requisite with binary search is that the array
# should be sorted. Without having a sorted array, we cannot
# implement binary search.

def binarySearchAlgo(arr: list[int], target: int):
    # Finding the length of the array
    n = len(arr)
    
    # Now initialising high and low
    high = n - 1
    low = 0

    while(low <= high):
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1

array = [1, 2, 4, 12, 467, 2342, 65, 12, 2]
# Sorting the array since the array should
# be sorted.
array.sort()

# Printing the sorted array for reference
print(array)

# 
element = int(input("Enter the element you want to search: "))

x = binarySearchAlgo(array, element)

if(x != -1):
    print("Element found at Index:", x)
else:
    print("Element doesn't exist in the array!")