# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.
#
# Constraints:
# -  The number of the nodes in the list is in the range [0, 10^4].
# -  -10^5 <= Node.val <= 10^5
# -  pos is -1 or a valid index in the linked-list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        
        h = head
        x = 0
        
        while h.next:
            x += 1
            h = h.next
            if x > 10000:
                return True
        
        return False


# Hash Table - Linked List - Two Pointers