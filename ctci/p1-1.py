"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""

def isUnique(str):
    seen = set()
    for c in str:
        if c in seen:
            return False
        seen.add(c)
    return True

assert isUnique('hello') == False
assert isUnique('stanford') == True

# Time Complexity: O(N) because we scan the input string once.
# Space Complexity: O(N) because our set grows with respect to how many unique characters are in the input string.

def isUniqueSol(str):
    alphabet = [False] * 128
    for c in str:
        if alphabet[ord(c)]:
            return False
        alphabet[ord(c)] = True
    return True

assert isUniqueSol('hello') == False
assert isUniqueSol('stanford') == True

# Time Complexity: O(N) because we scan the input string once.
# Space Complexity: O(1) because our alphabet is always a fixed size of 128 no matter what the size of our input string is.
