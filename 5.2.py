"""
Increment an Arbitrary-Precision Integer
Input:
    An array of digits that is non-negative. E.g. [1, 2, 9]
Output:
    The input array of digits incremented by 1. E.g. [1, 3, 0]
"""

def solution(A):
    """
    Start from the end of the array and recursively add one until we reach an element that is less than 9 or we hit the end of the array. If we hit the array of the array, we append a 1 to the front.
    """
    def helper(A, pos, carry):
        if not A and carry == 1:
            return [1]
        elif A[pos] < 9:
            A[pos] += carry
            return A
        A[pos] = 0
        return helper(A[:len(A) - 1], pos - 1, 1) + A[pos: len(A)]
    return helper(A, len(A) - 1, 0)
    
assert solution([1, 2, 9]) == [1, 3, 0]
assert solution([1, 9, 9]) == [2, 0, 0]
assert solution([9, 9, 9]) == [1, 0, 0, 0]

# Time Complexity: O(N) because in the worst case, our input array is all 9 and we traverse the entire array linearly.
# Space Complexity: O(N) because our recursive call stack can grow linearly with respect to the number of elements in our input array.

def solutionTwo(A):
    """
    We build off of our recursive solution and implement the function with constant space complexity.
    """
    pos = len(A) - 1
    carry = 1
    while pos >= 0: 
        if A[pos] < 9:
            A[pos] += carry
            return A
        A[pos] = 0
        pos -= 1
    return [carry] + A

assert solutionTwo([1, 2, 9]) == [1, 3, 0]
assert solutionTwo([1, 9, 9]) == [2, 0, 0]
assert solutionTwo([9, 9, 9]) == [1, 0, 0, 0]

# Time Complexity: O(N) because in the worst case, our input array is all 9 and we traverse the entire array linearly.
# Space Complexity: O(N) because we modify our input array in-place.
