# We will make a basic code to implement linear search.
# This will tell us about all the locations where the element
# exists. The indeces are stored in a list and the list is returned.

def linearSearch(arr: list[int], target: int) -> int:
    # Length of the array
    n = len(arr)
    index = []

    # Searching elements one by one.
    for iLoop in range(n):
        if arr[iLoop] == target:
            index.append(iLoop)
    
    return index

# Random Numbers 
array = [1, 2, 4, 12, 6, 467, 2342, 65, 12, 2, 4, 5, 2, 3, 5, 4]
x = linearSearch(array, 4)

if(x):
    print("Element found at Index:", x)
else:
    print("Element not found!!!")