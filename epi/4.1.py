"""
Computing The Parity of A Word
Input: 
    An integer x
Output:
    The parity of x
"""
def solution(x):
    """
    The intuition behind this approach is that we iteratively test each bit of x and return whether the number of counted set bits are odd or even.
    """
    count = 0
    while x > 0:
        count += x & 1
        x >>= 1
    if count % 2 == 1:
        return 1
    return 0

assert solution(5) == 0
assert solution(8) == 1
assert solution(13) == 1

# Time Complexity: O(N) where N is the number of bits in x, because we iterate through all the bits of x.
# Space Complexity: O(1) because we do not allocate any extra memory.

def solutionTwo(x):
    """
    The intuition behind this approach is that x & (x - 1) returns x wtih its least significant 1 bit cleared.
    """
    count = 0
    while x > 0:
        x &= (x - 1)
        count ^= 1
    return count

assert solutionTwo(5) == 0
assert solutionTwo(8) == 1
assert solutionTwo(13) == 1

# Time Complexity: O(k) where k is the number of 1 bits in x, because we clear the least significant 1 bit of x k times.
# Space Complexity: O(1) because we do not allocate any extra memory.

def solutionThree(x):
    """
    The intuition behind this approach is that the parity of a word is the XOR of all bits in the integer. XOR has the property of being associative and commutative which means it does not matter how we group the bits and the order we perform operations on them.
    """
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1

assert solutionThree(5) == 0
assert solutionThree(8) == 1
assert solutionThree(13) == 1

# Time Complexity: O(log N) where N is the number of bits in x, because we XOR the bit word of x with half of itself until we reach the base case of a word of 1 bit length.
# Space Complexity: O(1) because we do not allocate any extra memory.
