"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
"""

def oneAway(str1, str2):
    alphabet = [0] * 128
    for c in str1:
        alphabet[ord(c)] += 1
    for c in str2:
        if alphabet[ord(c)] > 0:
            alphabet[ord(c)] -= 1
        else:
            alphabet[ord(c)] += 1
    
    differences = 0
    for count in alphabet:
        differences += count
    
    return differences <= 2

assert oneAway("pale", "ple") == True
assert oneAway("pales", "pale") == True
assert oneAway("pale", "bale") == True
assert oneAway("pale", "bake") == False
