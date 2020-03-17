"""
Buy And Sell A Stock Twice
Input:
    An input array that represents stock prices over a period of days.
Output:
    The maximum profits achieveable by buying then selling two stocks.
"""

def solution(A):
    minSoFar, maxProfit = float('inf'), 0
    left = [0] * len(A)
    for i in range(len(A)):
        if A[i] < minSoFar:
            minSoFar = A[i]
        else:
            maxProfit = max(maxProfit, A[i] - minSoFar)
        left[i] = maxProfit
    
    right = [0] * len(A)
    maxSoFar, maxProfit = float('-inf'), 0
    for i in range(len(A) - 1, -1, -1):
        if A[i] > maxSoFar:
            maxSoFar = A[i]
        else:
            maxProfit = max(maxProfit, maxSoFar - A[i])
        right[i] = maxProfit
    
    maxProfit = 0
    for x, y in zip(left, right):
        maxProfit = max(maxProfit, x + y)
    return maxProfit

assert solution([1, 4, 5, 7, 6, 3, 2, 9]) == 13
assert solution([12,11,13,9,12,8,14,13,15]) == 10

# Time Complexity: O(N) because we traverse through the arrays 3 times, twice to calculate the left array (which is the best possible sale we can make from [0, j] where the minimum buy should occur in this range) and the right array (which is the best possible buy we can make from [j + 1, n]) where the maximum sell should occur in this range), and the final iteration to calculate the max profit.
# Space Complexity: O(N) because we allocate memory for left and right arrays.
