# Given the head of a linked list, return the list after sorting it in ascending order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Cut the linked list into two halves
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        
        # Recursion: Divide phase until you have 1 or 2 items (l, r)        
        l, r = self.sortList(head), self.sortList(second)
        # Merge sort: Conquer phase -> merge into (growing length) sorted lists
        return self.merge(l, r)
        
        
    def merge(self, l, r):
        if not l or not r:
            return l or r
        
        # Dummy head and pointer p
        dummy = p = ListNode(0)
        
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        
        p.next = l or r
        
        return dummy.next


# Linked List - Two Pointers - Divide and Conquer - Sorting - Merge Sort