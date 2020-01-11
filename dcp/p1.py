"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def mySolution(arr, k):
    complements = set()
    for num in arr:
        complement = k - num
        if complement in complements:
            return True
        else:
            complements.add(num)
    return False

arr = [10, 15, 3, 7]
k = 17
print(mySolution(arr, k))

# Time Complexity: O(N) because we iterate through all elements of the input array once in the worst case.
# Space Complexity: O(N) because at most, we add all elements of the input array into the set.

def givenSolution(array, k):
    potential_solutions = set()
    for num in array:
        if num in potential_solutions:
            return True
        potential_solutions.add(k - num)
    
    return False

arr = [10, 15, 3, 7]
k = 17
print(givenSolution(arr, k))

# Time Complexity: O(N) because we iterate through all elements of the input array once in the worst case.
# Space Complexity: O(N) because at most, we add all elements of the input array into the set.
