"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

mapping = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z'
}

def mySolution(msg, mapping, decoded):
    if (mapping == 0):
        return len(decoded)
    if (msg > 0):
        first = mapping[int(str(msg)[:1])]
        decoded.add(first)
    if (msg > 10):
        second = mapping[int(str(msg)[:2])]
        decoded.add(second)
    return mySolution(int(str(msg)[1::]), mapping, decoded) + mySolution(int(str(msg)[2::]), mapping, decoded)

def givenSolution(code):
    dp = [-1 for i in range(len(code))]
    return givenSolutionDP(code, 0, dp)

def givenSolutionDP(code, ptr, dp):
    if ptr >= len(code):
        return 1
    if dp[ptr] > -1:
        return dp[ptr]
    count = 0
    for i in range(1, 3):
        if (ptr + i <= len(code)):
            substring = code[ptr:ptr + i]
            if (givenSolutionIsValid(substring)):
                count += givenSolutionDP(code, ptr + i, dp)
    dp[ptr] = count
    return dp[ptr]

def givenSolutionIsValid(code):
    if len(code) == 0 or code[0] == '0':
        return False
    value = int(code)
    return value <= 26 and value >= 1

print(givenSolution('111'))

# Time Complexity: O(N) because we utilize memoization in our dynamic programming solution.
# Space Complexity: O(N) because our recursive call stack grows as large as our input.