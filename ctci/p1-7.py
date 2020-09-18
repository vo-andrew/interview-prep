"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""

def rotateMatrix(image):
    rotated = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]

    for x in range(len(image)):
        for y in range(len(image[x])):
            rotated[y][len(image) - x - 1] = image[x][y]
    return rotated

image = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

expected = [[7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]]

assert rotateMatrix(image) == expected

# Time Complexity: O(N^2) because we iterate through all elements of the input.
# Space Complexity: O(N^2) because we create a new copy of the rotated image.
