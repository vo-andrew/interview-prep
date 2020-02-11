"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def mySolution(arr):
    totalProduct = 1
    for num in arr:
        totalProduct *= num
    productArr = []
    i = 0
    while (i < len(arr)):
        productArr += [totalProduct // arr[i]]
        i += 1
    return productArr

arr = [1, 2, 3, 4, 5]
print(mySolution(arr))
        
# Time Complexity: O(N) because we iterate through all elements of the input array twice. Once to calculate the total product, and a second time to calculate the individual elements of the output array.
# Space Complexity: O(N) because the size of our output array will have to be the same size of our input array.

def givenSolution(arr):
    cumProd = 1
    leftArr = []
    for num in arr:
        cumProd *= num
        leftArr += [cumProd]
    
    cumProd = 1
    rightArr = []
    for num in arr[::-1]:
        cumProd *= num
        rightArr += [cumProd]
    rightArr = rightArr[::-1]

    outputArr = []
    for i in range(len(arr)):
        if i == 0:
            outputArr += [rightArr[i + 1]]
        elif i == len(arr) - 1:
            outputArr += [leftArr[i - 1]]
        else:
            outputArr += [leftArr[i - 1] * rightArr[i + 1]]
    return outputArr

arr = [1, 2, 3, 4, 5]
print(givenSolution(arr))

# Time Complexity: O(N) because we iterate through all elements of the input array three times. Once to calculate the cumulative product from left to right, a second time to calculate the cumulative product from right to left, and finally a third time to calculate the individual elements of the output array.
# Space Complexity: O(N) because the size of our cumulative product arrays and output array will have to be the same size of our input array.
