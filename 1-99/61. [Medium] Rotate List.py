# Given the head of a linked list, rotate the list to the right by k places.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        length = 1
        pointer = head
        
        while pointer.next:
            length += 1
            pointer = pointer.next
        
        k = k % length
        
        if k == 0:
            return head
        
        # Set the last node to point to head node
        # The list is now a circular linked list with last node pointing to first node
        pointer.next = head
        
        # Traverse the list to get to the node just before the (length - k)th node
        pointer = head
        for _ in range(length - k - 1):
            pointer = pointer.next
            
        # Get the next node from the pointer and then set the pointer.next as None
        answer = pointer.next
        pointer.next = None
        
        return answer