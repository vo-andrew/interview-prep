"""
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
"""

def mySolution(arr, k):
    for i in range(k + 1):
        max = arr[i]
        for j in range(i, k + i):
            if arr[j] > max:
                max = arr[j]
        print(max)

arr = [10, 5, 2, 7, 8, 7]
k = 3
mySolution(arr, k)

# Time Complexity: O(Nk) because there are N - k + 1 sliding windows and there are k elements in each window.
# Space complexity: O(1) because we do not allocate any extra memory.