"""
Variant
Input:
    An array with keys that can take on one of three values.
Output:
    A reordered array where all objects with the same key appear together.
"""

def solution(A):
    """
    The main intuition behind this approach is that we first do a linear pass of the array to track what are the three possible values of the keys. We then instantiate three arrays which will hold the distinct three elements we encounter. In the second pass, we reorder the elements of the array such that similar keys are grouped together by appending them to their respective array. At the end, we return the three arrays concatenated together.
    """
    if not A:
        return A
    pos = 0
    seen = list()
    for elem in A:
        if elem not in seen:
            seen.append(elem)
    first = list()
    second = list()
    third = list()
    for elem in A:
        if elem == seen[0]:
            first.append(elem)
        elif elem == seen[1]:
            second.append(elem)
        else:
            third.append(elem)
    first += second
    first += third
    return first

# Time Complexity: O(N) since we iterate through our input array twice. Once to keep track of the values of the keys. The second time to group similar keys together in their respective arrays.
# Space Complexity: O(N) since we instantiate three arrays for the three distinct values the keys can take on. Our output array has a length that scales linearly with the size of our input array.

assert solution([7, 2, 5, 5, 2, 7, 2, 2]) == [7, 7, 2, 2, 2, 2, 5, 5]

def solutionTwo(A):
    """
    The main intuition for this approach is that we want to make our space complexity O(1). We build off of our first solution by treating our input array as having 4 subarrays within it:
    First Key = A[:first]
    Second Key = A[first:second]
    Unclassified elements = A[second:third]
    Third Key = A[third:]
    """
    if not A:
        return A
    seen = list()
    for elem in A:
        if elem not in seen:
            seen.append(elem)
        if len(seen) == 3:
            break
    first = 0
    second = 0
    third = len(A)
    while second < third:
        if A[second] == seen[0]:
            A[first], A[second] = A[second], A[first]
            first += 1
            second += 1
        elif A[second] == seen[1]:
            second += 1
        else:
            third -= 1
            A[second], A[third] = A[third], A[second]
    return A

assert solutionTwo([7, 2, 5, 5, 2, 7, 2, 2]) == [7, 7, 2, 2, 2, 2, 5, 5]

# Time Complexity: O(N) since we iterate through our input array twice. Once to keep track of the values of the keys. The second time to group similar keys together in their respective arrays.
# Space Complexity: O(1) because we rearrange the elements of the array in-place without allocating extra memory for a new array.
