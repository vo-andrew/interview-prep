"""
Delete Duplicates From A Sorted Array
Input:
    A sorted array with duplicate values.
Output:
    An array with the duplicate values removed.
"""

def solution(A): 
    """
    We want to overwrite duplicate values with new values that we see in one pass.
    """
    available = 1     
    for i in range(1, len(A)):
        if A[available - 1] != A[i]: # We look at available - 1 because we know that a duplicate value can only be at the current position of available. available - 1 should be the start position of where the duplicates occur. Since a duplicate value can only occur at the current position of available, this makes A[available] a candidate for being overwritten. We cannot compare the value of the current element we are looking at to A[available] because A[available] is not necessarily a duplicate value.
            A[available] = A[i]
            available += 1
    return A

print(solution([2, 3, 5, 5, 7, 11, 11, 11, 13]))

# Time Complexity: O(N) because we traverse through the array in one pass.
# Space Complexity: O(1) because we do not allocate any extra memory to hold data.
