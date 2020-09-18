"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
"""

def isPalindromPermutation(input):
    alphabet = [0] * 128
    for c in input:
        if c != ' ':
            alphabet[ord(c.lower())] += 1
    seenOdd = False
    for letterCount in alphabet:
        if letterCount % 2 == 1:
            if seenOdd:
                return False
            seenOdd = True
    return True

assert isPalindromPermutation("raccare") == True
assert isPalindromPermutation("Tact Coa") == True
assert isPalindromPermutation("jadidakkk") == False
