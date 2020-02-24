"""
Computing The Parity of A Word
Input: 
    An integer x
Output:
    The parity of x
"""
def solution(x):
    count = 0
    while x > 0:
        count += x & 1
        x >>= 1
    if count % 2 == 1:
        return 1
    return 0

assert solution(5) == 0
assert solution(8) == 1

# Time Complexity: O(N) where N is the number of bits in x, because we iterate through all the bits of x.
# Space Complexity: O(1) because we do not allocate any extra memory.
