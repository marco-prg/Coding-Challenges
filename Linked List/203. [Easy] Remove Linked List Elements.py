# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        start = None
        previous = None
        current = head
        
        while current != None:
            if current.val != val:
                if not start:
                    start = current
                previous = current
            elif previous != None:
                previous.next = current.next
            current = current.next
            
        return start


# Linked List - Recursion