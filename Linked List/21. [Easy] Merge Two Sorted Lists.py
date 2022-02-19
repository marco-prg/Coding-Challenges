# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, a: ListNode, b: ListNode) -> ListNode:
        # a is always the smaller one        
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        # return the first not None between a and b
        return a or b


# Linked List - Recursion