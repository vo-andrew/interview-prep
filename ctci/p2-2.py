"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
"""

class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def kthToLast(lst, k):
    length = 0
    ptr = lst
    while ptr != None:
        ptr = ptr.next
        length += 1
    ptr = lst
    while ptr != None and length != k:
        ptr = ptr.next
        length -= 1
    return ptr.data

lst1 = LinkedList(1)
lst2 = LinkedList(2)
lst3 = LinkedList(3)
lst4 = LinkedList(4)
lst5 = LinkedList(5)
lst6 = LinkedList(6)
lst7 = LinkedList(7)

lst1.next = lst2
lst2.next = lst3
lst3.next = lst4
lst4.next = lst5
lst5.next = lst6
lst6.next = lst7

assert kthToLast(lst1, 3) == 5
assert kthToLast(lst1, 6) == 2

# Time Complexity: O(N) because we traverse through our linked list twice, once to calculate the length of the list, and the second time to find the kth to last element.
# Space Complexity: O(1) because we do not allocate any data structures to hold data.

def kthToLastSol(lst, k):
    ptr1 = lst
    ptr2 = lst
    for _ in range(k):
        if ptr1 == None:
            return None
        ptr1 = ptr1.next
    while ptr1 != None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr2.data

assert kthToLastSol(lst1, 3) == 5
assert kthToLastSol(lst1, 6) == 2
        
# Time Complexity: O(N) because we traverse through our linked list once.
# Space Complexity: O(1) because we do not allocate any data structures to hold data.
