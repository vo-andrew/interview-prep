"""
Compute The Levenshtein Distance
Input:
    Two strings a and b.
Output:
    The minimum number of edits to transform the first string into the second.
"""

def solution(a, b):
    def compute(aid, bid):
        if aid < 0:
            return bid + 1
        elif bid < 0:
            return aid + 1
        if dp[aid][bid] == -1:
            if a[aid] == b[bid]:
                dp[aid][bid] = compute(aid - 1, bid - 1)
            else:
                substitute = compute(aid - 1, bid - 1)
                insert = compute(aid - 1, bid)
                delete = compute(aid, bid - 1)
                dp[aid][bid] = 1 + min(substitute, insert, delete)
        return dp[aid][bid]
    dp = [[-1] * len(b) for _ in a]
    return compute(len(a) - 1, len(b) - 1)
    
print(solution('carthorse', 'orchestra'))

# Time Complexity: O(AB) because we have AB subproblems which take constant time to compute.
# Space Complexity: O(AB) because we allocate memory for our 2-D DP array which has dimensions len(A) * len(B).
