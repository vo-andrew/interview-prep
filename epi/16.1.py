"""
Count The Number Of Score Combinations
Input:
    A final score and scores for individual plays.
Output:
    The number of combinations of plays that result in the final score.
"""

def solution(finalScore, plays):
    """
    Use a bottom-up approach to build up to the final result.
    """
    dp = [[1] + [0] * finalScore for _ in plays]

    for i in range(len(plays)):
        for j in range(1, finalScore + 1):
            withoutPlay = dp[i - 1][j] if i >= 1 else 0
            withPlay = dp[i][j - plays[i]] if j >= i else 0
            dp[i][j] = withoutPlay + withPlay
    return dp[-1][-1]

assert solution(12, [2, 3, 7]) == 4

# Time Complexity: O(SN) where S is the number of possible plays and N is the size of the final score. We use a nested loop.
# Space Complexity: O(SN) because we create a dp array that stores our subproblem results.
