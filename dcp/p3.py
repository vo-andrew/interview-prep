"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mySolutionSerialize(node):
    if node is None:
        return ""
    return mySolutionSerialize(node.left) + " " + str(node.val) + " " + mySolutionSerialize(node.right)

def mySolutionDeserialize(str):
    if not str:
        return None
    str = str.split()
    child = Node(str[0])
    for i in range(1, len(str)):
        if (str[i] > child.val):
            child.right = Node(str[i])
        else:
            child = Node(str[i], child)
    return child

def givenSolutionSerialze(node):
    def func(node):
        if node:
            lst.append(node.val)
            func(node.left)
            func(node.right)
        else:
            lst.append('#')
    lst = []
    func(node)
    return " ".join(lst)

def givenSolutionDeserialze(str):
    def func():
        val = next(vals)
        if val == "#":
            return None
        else:
            node = Node(val)
            node.left = func()
            node.right = func()
            return node
    vals = iter(str.split())
    return func()

node = Node('root', Node('left', Node('left.left')), Node('right'))
print(givenSolutionDeserialze(givenSolutionSerialze(node)).left.left.val)

# Time Complexity: O(N) because we visit every node in our serialize function. It is also O(N) for deserialize because we iterate through our string and construct the binary tree from it.
# Space Complexity: O(N) because our recursive call stack can be as long as the depth of the tree.