"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self):
        return str(self.data)

def mySolution(tree):
    if tree is None:
        return 0
    if tree.left is None and tree.right is None:
        return 1
    left = mySolution(tree.left)
    right = mySolution(tree.right)
    if (tree.left.data == tree.data and tree.right.data == tree.data):
        return 1 + left + right
    return left + right

node_a = Node('0')
node_b = Node('1')
node_c = Node('0')
node_d = Node('1')
node_e = Node('0')
node_f = Node('1')
node_g = Node('1')
node_a.left = node_b
node_a.right = node_c
node_c.left = node_d
node_c.right = node_e
node_d.left = node_f
node_d.right = node_g

assert mySolution(None) == 0
assert mySolution(node_a) == 5
assert mySolution(node_c) == 4
assert mySolution(node_g) == 1
assert mySolution(node_d) == 3

# Time Complexity: O(N) because we visit every node in the tree.
# Space Complexity: O(N) because the size of our recursive call stack becomes the depth of the tree.
