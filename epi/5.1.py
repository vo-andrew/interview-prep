"""
The Dutch National Flag Problem
Input:
    An array A and an index i
Output:
    A paritioned array with its elements rearranged in an order where elements < a[i] appear first, elements = a[i] appear next, followed by elements > a[i] after.
"""

def solution(A, i):
    """
    The main intuition behind this brute force approach is that we create a new output array that we populate with the elements from our input array in their partitioned order with 3 passes.
    """
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
    """
    The main intuition behind this approach is that we perform three passes of our input array to partition our elements keeping track of an available spot in our array where we can place elements. In the first pass, we arrange elements that are smaller than the pivot towards the front of the array. In the second pass, we update the index where we place our elements if the current element we are looking at is equal to the pivot. Finally, in the third pass, we arrange elements that are bigger than the pivot at the remaining available positions in our array and update the remaining available spots.
    """
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
    """
    The main intuition behind this approach is that we want to partition our array in one pass. We maintain pointers towards the ends of the array which represent indicies where our smaller/larger elements will be placed. We use a while loop instead of a for loop because swapping elements may cause the current element we are looking at to be smaller/larger than the pivot.
    """
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

def solutionFour(A, i):
    """
    The main intuition beind this approach is that we first put elements smaller than the pivot towards the front of the array in one pass. We then put elements greater than the pivot towards the end of the array. Using this approach, elements equal to the pivot are placed in the middle automatically.
    """
    if not A or i >= len(A):
        return A
    pivot = A[i]
    smaller, larger = 0, len(A) - 1
    for k in range(len(A)):
        if A[k] < pivot:
            A[k], A[smaller] = A[smaller], A[k]
            smaller += 1
    for k in reversed(range(len(A))):
        if A[k] < pivot:
            break
        elif A[k] > pivot:
            A[k], A[larger] = A[larger], A[k]
            larger -= 1
    return A

assert solutionFour([6, 3, 7, 1, 3, 6, 9], 4) == [1, 3, 3, 7, 6, 6, 9]

# Time Complexity: O(N) because we perform 2 linear traversals of our input array. Our first pass places elements smaller than the pivot to the front of the array. The second pass places elements greater than the pivot to the end of the array.
# Space Complexity: O(1) because we rearrange the elements of the array in-place without allocating extra memory for a new array.

def solutionFive(A, i):
    """
    The main intuition behind this approach is that we maintain four subarrays within our input array:
    Elements less than pivot: A[:smaller]
    Elements equal to pivot: A[smaller:equal]
    Unclassified elements: A[equal:larger]
    Elements larger than pivot: A[larger:]
    We swap elements into their respective partitions until there are no more unclassified elements.
    """
    if not A or i >= len(A):
        return A
    pivot = A[i]
    smaller, equal, larger = 0, 0, len(A) - 1
    while equal <= larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        else:
            A[equal], A[larger] = A[larger], A[equal]
            larger -=1
    return A

assert solutionFive([6, 3, 7, 1, 3, 6, 9], 4) == [1, 3, 3, 7, 6, 9, 6]

# Time Complexity: O(N) because we perform one linear traveral of the array to create each respective partition of our output array.
# Space Complexity: O(1) because we rearrange the elements of the array in-place without allocating extra memory for a new array.
