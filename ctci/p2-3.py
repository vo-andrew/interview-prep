class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

"""
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
"""

def solution(list_node):
    if not list_node or not list_node.next:
        return
    list_node.val = list_node.next.val
    list_node.next = list_node.next.next

first = ListNode('a')
second = ListNode('b')
third = ListNode('c')
fourth = ListNode('d')
fifth = ListNode('e')
sixth = ListNode('f')

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth

solution(third)

ptr = first
while ptr:
    print(ptr.val)
    ptr = ptr.next
    