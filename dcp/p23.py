"""
You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
"""
from copy import deepcopy


def add_to_cache(coordinate, cache):
    new_cache = deepcopy(cache)
    new_cache.add("{}-{}".format(coordinate[0], coordinate[1]))
    return new_cache


def is_visited(coordinate, cache):
    return "{}-{}".format(coordinate[0], coordinate[1]) in cache


def find_path(matrix, rows, cols, start, end, cache):
    if start == end:
        return 0

    cache = add_to_cache(start, cache)

    def explore_neighbour(coordinate):
        if not is_visited(coordinate, cache) and \
                matrix[coordinate[0]][coordinate[1]] != "t":
            path_length = find_path(matrix, rows, cols, coordinate, end, cache)
            if path_length != None:
                path_lengths.append(path_length)

    path_lengths = list()
    if start[0] != 0:
        coordinate = (start[0] - 1, start[1])
        explore_neighbour(coordinate)
    if start[0] != rows - 1:
        coordinate = (start[0] + 1, start[1])
        explore_neighbour(coordinate)
    if start[1] != 0:
        coordinate = (start[0], start[1] - 1)
        explore_neighbour(coordinate)
    if start[1] != cols - 1:
        coordinate = (start[0], start[1] + 1)
        explore_neighbour(coordinate)

    return min(path_lengths) + 1 if path_lengths else None


matrix = [["f", "f", "f", "f"],
          ["t", "t", "f", "t"],
          ["f", "f", "f", "f"],
          ["f", "f", "f", "f"]]
assert find_path(matrix, len(matrix), len(
    matrix[0]), (0, 0), (0, 0), set()) == 0
assert find_path(matrix, len(matrix), len(
    matrix[0]), (1, 0), (0, 0), set()) == 1
assert find_path(matrix, len(matrix), len(
    matrix[0]), (3, 0), (0, 0), set()) == 7
assert find_path(matrix, len(matrix), len(
    matrix[0]), (3, 0), (0, 3), set()) == 6

matrix = [["f", "f", "f", "f"],
          ["t", "t", "t", "f"],
          ["f", "f", "f", "f"],
          ["f", "f", "f", "f"]]
assert find_path(matrix, len(matrix), len(
    matrix[0]), (0, 0), (0, 0), set()) == 0
assert find_path(matrix, len(matrix), len(
    matrix[0]), (1, 0), (0, 0), set()) == 1
assert find_path(matrix, len(matrix), len(
    matrix[0]), (3, 0), (0, 0), set()) == 9
assert find_path(matrix, len(matrix), len(
    matrix[0]), (3, 0), (0, 3), set()) == 6
assert find_path(matrix, len(matrix), len(
    matrix[0]), (2, 0), (3, 3), set()) == 4

# Time Complexity: O(N) because we traverse through the entire matrix in the worst case.
# Space Complexit: O(N) because our call stack can be as deep as the DFS path.