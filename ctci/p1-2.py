"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
"""

def checkPermutation(str1, str2):
    alphabet = [0] * 128
    for c in str1:
        alphabet[ord(c)] += 1
    for c in str2:
        alphabet[ord(c)] += 1
    for occurrence in alphabet:
        if occurrence % 2 == 1:
            return False
    return True

assert checkPermutation('hello', 'elhlo') == True
assert checkPermutation('racecar', 'yelp') == False
assert checkPermutation('god     ', 'dog') == False
assert checkPermutation('God', 'dog') == False

# Time Complexity: O(N) because we scan both input strings once and scan our alphabet once.
# Space Complexity: O(1) because our alphabet is always a fixed size of 128 no matter what the size of our input strings are. 

def checkPermutationSol(str1, str2):
    if (len(str1) != len(str2)):
        return False
    alphabet = [0] * 128
    for c in str1:
        alphabet[ord(c)] += 1
    for c in str2:
        alphabet[ord(c)] -= 1
        if alphabet[ord(c)] < 0:
            return False
    return True

assert checkPermutationSol('hello', 'elhlo') == True
assert checkPermutationSol('racecar', 'yelp') == False
assert checkPermutationSol('god     ', 'dog') == False
assert checkPermutationSol('God', 'dog') == False

# Time Complexity: O(N) because we scan both input strings once.
# Space Complexity: O(1) because our alphabet is always a fixed size of 128 no matter what the size of our input strings are. 
