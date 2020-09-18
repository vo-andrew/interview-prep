"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
"""

def URLify(input):
    result = []
    for c in input:
        if c != ' ':
            result.append(c)
        else:
            result.append('%')
            result.append('2')
            result.append('0')
    return ''.join(result)

assert URLify("Mr John Smith") == "Mr%20John%20Smith"

# Time Complexity: O(N) because we scan through each character of our input string.
# Space Complexity: O(N) because we need to construct our new resulting string with a character array.
