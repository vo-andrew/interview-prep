"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""
import time

def mySolution(f, n):
    time.sleep(n // 1000)
    f()

def testFunction():
    print("Hi")

mySolution(testFunction, 5000)

# Time Complexity: O(N + F) where N represents the number of milliseconds and F represents the time complexity of the input function.
# Space Complexity: O(F) where F represents the space complexity of the input function.