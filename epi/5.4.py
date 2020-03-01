"""
Advancing Through An Array
Input:
    An array of integers where each A[i] represents the maximum we can advance from index i.
Output:
    A boolean that says whether or not we can reach the end of the array.
"""

def solution(A):
    """
    We want to iterate through the list and keep track of the maximum possible position we can reach from each position in the array. At some index i, we can reach i + A[i].
    """
    furthest, goal = 0, len(A) - 1
    i = 0
    while i <= furthest and furthest < goal:
        furthest = max(furthest, i + A[i])
        i += 1
    return furthest >= goal

assert solution([3, 3, 1, 0, 2, 0, 1]) == True
assert solution([3, 2, 0, 0, 2, 0, 1]) == False

# Time Complexity: O(N) because we iterate through the array once, keeping track of the farthest index we can reach.
# Space Complexity: O(1) because we do not allocate any extra memory.
