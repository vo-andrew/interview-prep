"""
Replace and Remove
Input:
    An array of characters and an integer representing how many entries in the array are applied the operation.
Output:
    The array with its 'a's replaced with two 'd's and each 'b' deleted.
"""

def solution(A, x):
    """
    Brute-force solution with array insert and pop functions. 
    """
    pos = 0
    while pos < len(A):
        if A[pos] == 'a':
            A[pos] = 'd'
            A.insert(pos + 1, 'd')
            pos += 1
        elif A[pos] == 'b':
            A.pop(pos)
        else:
            pos += 1
    return A

assert solution(['a', 'c', 'd', 'b', 'b', 'c', 'a'], 7) == ['d', 'd', 'c', 'd', 'c', 'd', 'd']

# Time Complexity: O(N^2) because insert and pop functions can take at most O(N) to shift elements after performing their operation. Since we perform these O(N) operations O(N) times, this is an overall runtime of O(N^2).
# Space Complexity: O(1) because we modify the input array in-place.

def solutionTwo(A, x):
    """
    Avoids using built-in array functions at the cost of additional space complexity.
    """
    result = list()
    for elem in A:
        if elem == 'a':
            result += ['d', 'd']
        elif elem != 'b':
            result += [elem]
    return result

assert solutionTwo(['a', 'c', 'd', 'b', 'b', 'c', 'a'], 7) == ['d', 'd', 'c', 'd', 'c', 'd', 'd']

# Time Complexity: O(N) because we do one traversal through the input array.
# Space Complexity: O(N) because we allocate memory for our output array.

def solutionThree(s, size):
    """
    Do one forward pass to remove all 'b's and count the number of 'a's. Do another second pass backwards that replaces all 'a's with 'dd's. 
    """
    write = 0
    acount = 0
    for elem in s:
        if elem != 'b':
            s[write] = elem
            write += 1
        if elem == 'a':
            acount += 1

    curr = write - 1
    write += acount - 1
    while curr >= 0:
        if s[curr] == 'a':
            s[write - 1 : write + 1] = 'dd'
            write -= 2
        else:
            s[write] = s[curr]
            write -= 1
        curr -= 1
    return s

assert solutionThree(['a', 'c', 'd', 'b', 'b', 'c', 'a'], 7) == ['d', 'd', 'c', 'd', 'c', 'd', 'd']

# Time Complexity: O(N) because we do 2 linear passes of our input array.
# Space Complexity: O(1) because we modify the input array in-place.
