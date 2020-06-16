# TO-DO: Complete the selection_sort() function below
'''
Algorithm

1. Start with current index = 0

2. For all indices EXCEPT the last index:

    a. Loop through elements on right-hand-side 
    of current index and find the smallest element

    b. Swap the element at current index with the
    smallest element found in above loop
'''
def selection_sort(arr):

    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        #Set min_idx to i
        min_idx = i

        #Loop throgh arr starting at i + 1
        for a in range(i + 1, len(arr)):
            #If arr[min_idx] is greater than arr[a]
            #set min_idx to a
            if arr[min_idx] > arr[a]:
                min_idx = a

        #Swap places in array
        arr[min_idx], arr[i] = arr[i], arr[min_idx]

    return arr


# TO-DO:  implement the Bubble Sort function below
'''
Algorithm

1. Loop through your array
    - Compare each element to its neighbor
    - If elements in wrong position (relative to each other, swap them)
2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
'''
def bubble_sort(arr):
    # loop through array and compare arr[i] to arr[i + 1]
    # if arr[i] < arr[i + 1] swap positions in arr
    # where arr[i] becomes arr[i +1] and arr[i + 1] becomes arr[i]
    # if no swap stop else reset index to 0 and loop again

    #Loop until break statement encountered
    while True:
        #Set count to zero
        count = 0
        #Loop through array n - 1 times
        for i in range(len(arr) - 1):
            #Check if i is greater than i + 1
            if arr[i] > arr[i + 1]:
                #Swap places in array
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
                #Increment count by 1
                count += 1
                
        #Check to see if any swaps were made
        if count == 0:
            #Break out of loop
            break



    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''

#https://ayada.dev/posts/counting-sort/
def counting_sort(arr, maximum=None):
    n = len(arr)

    #Check that array is not empty
    if len(arr) > 0:
        #Set maximum to max value in array + 1
        maximum = max(arr) + 1
    else:
        #If the array is empty set maximum to 0 
        maximum = 0

    temp_arr = [0] * maximum

    for v in arr:
        temp_arr[v] += 1
        

    s = 0

    for i in range(0, maximum):
        tmp = temp_arr[i]
        temp_arr[i] = s
        s += tmp


    result = [None] * n

    for v in arr:
        #Check for negative numbers in array
        if min(arr) >= 0:
            result[temp_arr[v]] = v
            temp_arr[v] += 1
        else:
            #If there is a negative number send expected error message
            result = 'Error, negative numbers not allowed in Count Sort'
        

    arr = result

    return arr
