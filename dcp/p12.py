"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

def mySolutionHelper(n, pos, dp):
    if pos < 0:
        return 0
    if dp[pos] > -1:
        return dp[pos]
    result = mySolutionHelper(n, pos - 1, dp) + mySolutionHelper(n, pos - 2, dp)
    dp[pos] = result
    return result

def mySolution(n):
    dp = [-1 for x in range(n)]
    dp[0] = 1
    dp[1] = 2
    return mySolutionHelper(n, n - 1, dp)

print(mySolution(4))

# Time Complexity: O(N) because our recursive call stack will only fill up the values of our dp array which has length based on the input value. There will be no repeat calls because of memoization.
# Space Complexity: O(N) because our recursive call stack has depth based on the input value.

