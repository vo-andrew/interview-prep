"""
Count The Number Of Score Combinations
Input:
    A final score and scores for individual plays.
Output:
    The number of combinations of plays that result in the final score.
"""

def solution(s, p):
    dp = [[1] + [0] * s for _ in p]
    for i in range(len(p)):
        for j in range(1, s + 1):
            withoutPlay = dp[i - 1][j] if i >= 1 else 0
            withPlay = dp[i][j - p[i]] if j >= p[i] else 0
            dp[i][j] = withoutPlay + withPlay
    return dp[-1][-1]

print(solution(12, [2, 3, 7]))

# Time Complexity: O(SN) because we iterate through an S X N DP array that holds our subproblems. In addition, we explore every possible play combination for every score.
# Space Complexity: O(SN) because we our DP array holds O(SN) subproblems.
