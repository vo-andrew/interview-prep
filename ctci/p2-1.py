"""
Remove Dups! Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""

class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeDups(lst):
    if lst is None:
        return lst
    seen = set()
    ptr = lst
    seen.add(ptr.data)
    while ptr != None and ptr.next != None:
        if ptr.next.data in seen:
            ptr.next = ptr.next.next
        seen.add(ptr.next.data)
        ptr = ptr.next
    return lst

lst = LinkedList(1)
lst.next = LinkedList(2)
lst.next.next = LinkedList(1)
lst.next.next.next = LinkedList(3)
lst = removeDups(lst)
ptr = lst
while ptr != None:
    print(ptr.data)
    ptr = ptr.next
            
# Time Complexity: O(N) because we have to scan through the entire linked list once to check if there are any duplicate values.
# Space Complexity: O(N) because our set keeps track of how many unique numbers of our input list it has seen already, which grows linearly with respect to the size of our input list.

def removeDupsSol(lst):
    seen = set()
    previous = None
    while lst != None:
        if lst.data in seen:
            previous.next = lst.next
        else:
            seen.add(lst.data)
            previous = lst
        lst = lst.next
    return lst

lst = LinkedList(1)
lst.next = LinkedList(2)
lst.next.next = LinkedList(1)
lst.next.next.next = LinkedList(3)
lst = removeDups(lst)
ptr = lst
while ptr != None:
    print(ptr.data)
    ptr = ptr.next

# Time Complexity: O(N) because we have to scan through the entire linked list once to check if there are any duplicate values.
# Space Complexity: O(N) because our set keeps track of how many unique numbers of our input list it has seen already, which grows linearly with respect to the size of our input list.
