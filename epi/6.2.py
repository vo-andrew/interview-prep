"""
Base Conversion
Input:
    A string, an integer b1, an integer b2
Output:
    The string converted from base b1 to base b2.
"""

def solution(s, b1, b2):
    """
    Convert the string in base b1 to base 10. Convert the result in base 10 to base b2.
    """
    power = 0
    total = 0
    for c in reversed(s):
        digit = ord(c) - ord('0')
        total += digit * (b1 ** power)
        power += 1
    
    characters = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

    result = []
    while total:
        digit = total % b2
        if digit in characters:
            digit = characters[digit]
        else:
            digit = str(digit)
        result.append(digit)
        total //= b2
    
    return ''.join(reversed(result))
    
assert solution('615', 7, 13) == '1A7'

# Time Complexity: O(N) because we traverse through every character of the input string.
# Space Complexity: O(1) because we have a constant amount of allocated space no matter the input size.
