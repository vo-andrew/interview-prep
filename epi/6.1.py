"""
Interconvert Strings And Integers
Input:
    An integer or a string of an integer.
Output:
    A string of an integer or an integer respectfully.
"""

def intToString(x):
    """
    Utilize the ord() function which returns the unicode value of a character. ord('0') = 48. Thus, if we add the least significant digit of x to ord('0'), and convert it back to a character using chr(), we get back the string representation of the least significant digit.
    """
    neg = False
    if x < 0:
        x, neg = -x, True
    
    s = []
    while x:
        s.append(chr(ord('0') + x % 10))
        x //= 10
    
    return '-' if neg else ''.join(reversed(s))

assert intToString(123) == '123'

# Time Complexity: O(N) because we traverse through every digit of the input integer.
# Space Complexity: O(N) because we allocate memory for every digit of our return output.

def stringToInt(s):
    """
    Traverse through the characters of the string from left to right. For every character, subtract its ord value from ord('0'). This returns the integer format of the character. Append this integer to our return output.
    """
    neg = False
    value = 0
    
    for c in s:
        if c == '-':
            neg = True
            continue
        digit = ord(c) - ord('0')
        value += digit
        value *= 10
    value //= 10
    if neg:
        value *= -1
    return value

assert stringToInt('123') == 123
assert stringToInt('-123') == -123
    
# Time Complexity: O(N) because we traverse through every character of the string once.
# Space Complexity: O(1) because we do not allocate any extra memory besides integer variables.
