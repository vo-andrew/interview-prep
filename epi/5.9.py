"""
Enumerate All Primes to N
Input: 
    n: 18
Output:
    return: [2,3,5,7,11,13,17]
"""
from math import floor

def is_prime(n):
    if n < 2:
        return False
    sqrt = n ** (1/2)
    for start in range(2, floor(sqrt) + 1):
        if n % start == 0:
            return False
    return True

def my_solution(n):
    res = list()
    if n < 2:
        return res
    for i in range(2, n):
        if is_prime(i):
            res.append(i)
    return res

print(my_solution(18))

# Time Complexity: O(N^(3/2)) because our main solution runs in linear time with respect to our input n. In our main solution, we call is_prime n times. is_prime has a time complexity of O(N^(1/2)) because we only check up to the square root of n to see if it is prime. Therefore, we multiply these complexities together.
# Space Complexity: O(1) because we do not allocate any extra memory.

def generate_primes(n):
    primes = []
    is_prime = [False, False] + [True] * (n - 1)
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i, n + 1, i):
                is_prime[j] = False
    return primes

print(generate_primes(18))

# Time Complexity: O(N log log N) because the time to remove multiples of i is proportional to n / i. Thus, the overal time complexity is O(n / 2 + n / 3 + n / 5 + n / 7 + n / 11 + ...). This sum asymptotically tends to n log log n.
# Space Complexity: O(N) because we allocate memory to store a boolean array corresponding to the first n natural numbers. 
