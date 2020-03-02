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
        if A[available - 1] != A[i]:
            A[available] = A[i]
            available += 1
    return A

print(solution([2, 3, 5, 5, 7, 11, 11, 11, 13]))

# Time Compelxity: O(N) because we traverse through the array in one pass.
# Space Complexity: O(1) because we do not allocate any extra memory to hold data.
