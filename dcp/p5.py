"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def mySolutionCar(pair):
    return pair[0]

def mySolutionCdr(pair):
    return pair[1]

def givenSolutionCar(f):
    def car(x, y):
        return x
    return f(car)
    
def givenSolutionCdr(f):
    def cdr(x, y):
        return y
    return f(cdr)

print(givenSolutionCar(cons(3, 4)))
print(givenSolutionCdr(cons(3, 4)))

# Time Complexity: O(1) because we are simply returning the first or last element of the pair.
# Space Complexity: O(1) because we do not create any data structures, we are only returning.