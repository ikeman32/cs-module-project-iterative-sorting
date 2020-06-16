def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    #Set high and low
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        #Set mid range
        mid = low + high // 2

        #If less than target ignore everything on the left
        if arr[mid] < target:
            low = mid + 1
        #if greater than target ignore everythin on the right
        elif arr[mid] > target:
            high = mid - 1
        #Otherwise return the result
        else:
            return mid

    return -1  # not found
