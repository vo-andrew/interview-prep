"""
Buy And Sell A Stock Once
Input:
    An input array that represents stock prices over a period of days.
Output:
    The maximum profits achieveable by buying then sellling one stock.
"""

def solution(A):
    if not A:
        return 0
    minSoFar = A[0]
    maxProfit = 0
    for elem in A:
        if elem < minSoFar:
            minSoFar = elem
        else:
            maxProfit = max(maxProfit, elem - minSoFar)
    return maxProfit

assert solution([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]) == 30

# Time Complexity: O(N) because we traverse through the input array linearly once.
# Space Complexity: O(1) because we only instantiate variables to track the minimum price we have seen the the maximum profit achieveable.
