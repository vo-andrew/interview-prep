"""
Interconvert Strings And Integers
Input:
    An integer or a string of an integer.
Output:
    A string of an integer or an integer respectfully.
"""

def intToString(x):
    neg = False
    if x < 0:
        x, neg = -x, True
    
    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break
    
    return '-' if neg else ''.join(reversed(s))

assert intToString(123) == '123'

# Time Complexity: O(N) because we traverse through the string once.
# Space Complexity: O(N) because we allocate memory for our return output.
    