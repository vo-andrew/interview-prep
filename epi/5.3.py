"""
Multiply Two Arbitrary-Precision Integers
Input:
    Two arrays representing integers.
Output:
    An array representing the product of the two integer representation arrays.
"""

def solution(A, B):
    """
    We perform elementary multiplication using an array to keep track of intermediate values and return the result. The maximum length of the product of two numbers A and B is len(A) + len(B).
    """
    # Handle negative cases
    sign = -1 if (A[0] < 0) ^ (B[0] < 0) else 1
    A[0], B[0] = abs(A[0]), abs(B[0])

    product = [0] * (len(A) + len(B))
    start = len(product) - 1
    offset = 0
    for i in reversed(range(len(A))):
        index = start - offset
        for j in reversed(range(len(B))):
            value = product[index] + (A[i] * B[j])
            product[index] = value % 10
            if value > 9:
                product[index - 1] += value // 10
            index -= 1
        offset += 1

    if product[0] == 0:
        product = product[1:]
    return [sign * product[0]] + product[1:]

assert solution([1, 0], [1, 0]) == [1, 0, 0]
assert solution([7, 2, 1], [5, 3]) == [3, 8, 2, 1, 3]
assert solution([9, 9, 9], [9, 9, 9]) == [9, 9, 8, 0, 0, 1]
assert solution([1, 9, 3, 7, 0, 7, 7, 2, 1], [-7, 6, 1, 8, 3, 2, 5, 7, 2, 8, 7]) == [-1, 4, 7, 5, 7, 2, 8, 5, 1, 4, 7, 4, 2, 1, 4, 1, 2, 9, 2, 7]

# Time Complexity: O(NM) where len(A) = N and len(B) = M because for every element of A, we multiply it with every element of B.
# Space Complexity: O(N + M) because the maximum size of our array output which stores the product of A and B is len(A) = N and len(B) = M.
 
def solutionTwo(A, B):
    """
    Cleaner way of implementing the solution.
    """
    sign = -1 if (A[0] < 0) ^ (B[0] < 0) else 1
    A[0], B[0] = abs(A[0]), abs(B[0])

    product = [0] * (len(A) + len(B))
    for i in reversed(range(len(A))):
        for j in reversed(range(len(B))):
            product[i + j + 1] += A[i] * B[j]
            product[i + j] += product[i + j + 1] // 10
            product[i + j + 1] %= 10
    
    nonZero = 0
    for elem in product:
        if elem != 0:
            break
        nonZero += 1
    product = product[nonZero:]
    
    return [sign * product[0]] + product[1:]

assert solutionTwo([1, 0], [1, 0]) == [1, 0, 0]
assert solutionTwo([7, 2, 1], [5, 3]) == [3, 8, 2, 1, 3]
assert solutionTwo([9, 9, 9], [9, 9, 9]) == [9, 9, 8, 0, 0, 1]
assert solutionTwo([1, 9, 3, 7, 0, 7, 7, 2, 1], [-7, 6, 1, 8, 3, 2, 5, 7, 2, 8, 7]) == [-1, 4, 7, 5, 7, 2, 8, 5, 1, 4, 7, 4, 2, 1, 4, 1, 2, 9, 2, 7]

# Time Complexity: O(NM) where len(A) = N and len(B) = M because for every element of A, we multiply it with every element of B.
# Space Complexity: O(N + M) because the maximum size of our array output which stores the product of A and B is len(A) = N and len(B) = M.
