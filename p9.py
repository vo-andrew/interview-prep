"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""
def mySolution(arr):
    if len(arr) == 0:
        return 0
    prev1 = 0
    prev2 = 0
    for num in arr:
        temp = prev1
        prev1 = max(prev2 + num, prev1)
        prev2 = temp
    return prev1

print(mySolution([5, 1, 1, 5]))

# Time Complexity: O(N) because we iterate through the input array once.
# Space Complexity: O(1) because we do not create any recursive calls or allocate extra memory.