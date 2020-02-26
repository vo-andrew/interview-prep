"""
The Dutch National Flag Problem
Input:
    An array A and an index i
Output:
    A paritioned array with its elements rearranged in an order where elements < a[i] appear first, elements = a[i] appear next, followed by elements > a[i] after.
"""

def solution(A, i):
    if not A:
        return A
    elif i >= len(A):
        return A
    pivot = A[i]
    output = list()
    for elem in A:
        if elem < pivot:
            output.append(elem)
    for elem in A:
        if elem == pivot:
            output.append(elem)
    for elem in A:
        if elem > pivot:
            output.append(elem)
    return output

assert solution([6, 3, 7, 1, 3, 6, 9], 4) == [1, 3, 3, 6, 7, 6, 9]

# Time Complexity: O(N) because we perform three linear traverals of the array to create each respective partition of our output array.
# Space Complexity: O(N) because we allocate memory for our output array which grows in size with respect to our input array.

def solutionTwo(A, i):
    if not A or i >= len(A):
        return A
    pos = 0
    pivot = A[i]
    for k in range(len(A)):
        if A[k] < pivot:
            A[pos], A[k] = A[k], A[pos]
            pos += 1
    for k in range(pos, len(A)):
        if A[k] == pivot:
            A[pos], A[k] = A[k], A[pos]
            pos += 1
    for k in range(pos, len(A)):
        if A[k] > pivot:
            A[pos], A[k] = A[k], A[pos]
            pos += 1
    return A
    
assert solutionTwo([6, 3, 7, 1, 3, 6, 9], 4) == [1, 3, 3, 6, 7, 6, 9]

# Time Complexity: O(N) because we perform three linear traverals of the array to create each respective partition of our output array.
# Space Complexity: O(1) because we rearrange the elements of the array in-place without allocating extra memory for a new array.

def solutionThree(A, i):
    if not A or i >= len(A):
        return A
    start = 0
    end = len(A) - 1
    pivot = A[i]
    pos = 0
    while pos < len(A) and start < end and pos <= end:
        if A[pos] < pivot:
            A[start], A[pos] = A[pos], A[start]
            start += 1
        elif A[pos] == pivot:
            pos += 1
        else:
            A[pos], A[end] = A[end], A[pos]
            end -= 1
    return A

assert solutionThree([6, 3, 7, 1, 3, 6, 9], 4) == [1, 3, 3, 7, 6, 9, 6]

# Time Complexity: O(N) because we perform one linear traveral of the array to create each respective partition of our output array.
# Space Complexity: O(1) because we rearrange the elements of the array in-place without allocating extra memory for a new array.
