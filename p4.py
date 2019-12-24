"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""
def mySolution(arr):
    for i in range(len(arr)):
        elem = arr[i]
        if elem > 0:
            arr[elem - 1] = elem
    
def givenSolutionSegregate(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] <= 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr[j::]

def givenSolutionFindMissing(arr):
    for num in arr:
        num = abs(num)
        if (num - 1 < len(arr)) and (arr[num - 1] > 0): # check index out of bounds and if previously marked, if it was previously marked, then we do not want to negate the negation.
            arr[num - 1] = -arr[num - 1]

    for i in range(len(arr)):
        if arr[i] > 0:
            return i + 1
    return len(arr) + 1 # if there is no missing number, the next logical missing number is the one that follows the sequence.

def givenSolution(arr):
    positives = givenSolutionSegregate(arr)
    return givenSolutionFindMissing(positives)

arr = [3, 4, -1, 1]
print(givenSolution(arr))
        
# Time Complexity: O(N) because we iterate throguh the entire input array in our segregate function and find missing function.
# Space Complexity: O(1) because we only modify the input array.