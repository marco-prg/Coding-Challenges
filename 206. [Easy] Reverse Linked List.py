# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Recursive solution
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(head)
    
    def reverse(self, current, prev=None):
        if not current:
            return prev
        
        nextn = current.next
        current.next = prev
        return self.reverse(nextn, current)
    
    # Iterative solution
    # def reverseList(self, head):
    # prev = None
    # while head:
    #     curr = head
    #     head = head.next
    #     curr.next = prev
    #     prev = curr
    # return prev
        