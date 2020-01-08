"""
Delete Duplicates From A Sorted Array
Input: 
    arr: [2,3,5,5,7,11,11,11,13]
Output: 
    return: 6
    arr: [2,3,5,7,11,13,0,0,0]
"""
"""
len = 6
duplicate = 3
[2,3,5,7,11,13,13,13,13]
"""
def mySolution(arr):
    if arr is None or len(arr) < 2:
       return 0 
    window = len(arr)
    duplicates = 0
    i = 1
    # for i in range(1, window): This causes an infinite loop. Window is not being updated somehow.
    while i < window:
        while arr[i] == arr[i - 1]:
            window -= 1
            duplicates += 1
            for j in range(i, window):
                arr[j] = arr[j + 1]
        i += 1
    return len(arr) - duplicates
            
arr = [2,3,5,5,7,11,11,11,13]
print(mySolution(arr))
print(arr)

# Time Complexity: O(N^2) because the number of shifts we have to do is (n - 1) + (n - 2) + ... + 2 + 1.
# Space Complexoty: O(1) because we do not allocate any extra memory.

def delete_duplicates(A):
    if not A:
        return 0
    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index

arr = [2,3,5,5,7,11,11,11,13]
print(delete_duplicates(arr))
print(arr)

# Time Complexity: O(N) because we have reduced the number of shifts needed when writing over duplicate values.
# Space Complexity: O(1) because we do not allocate any extra memory.