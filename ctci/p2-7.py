class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)

"""
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.
"""

def solution(a, b):
    a_length = 0
    b_length = 0
    ptr_a = a
    while ptr_a:
        ptr_a = ptr_a.next
        a_length += 1
    ptr_b = b
    while ptr_b:
        ptr_b = ptr_b.next
        b_length += 1
    difference = abs(a_length - b_length)
    if a_length >= b_length:
        for _ in range(difference):
            a = a.next
    else:
        for _ in range(difference):
            b = b.next
    while a.next:
        if a == b:
            return a
        a = a.next
        b = b.next
    return None

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d

e = ListNode(5)
e.next = c

print(solution(a, e))
