# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        mergedList = []
        while l1:            
            mergedList.append(l1.val)
            l1 = l1.next
        while l2:
            mergedList.append(l2.val)
            l2 = l2.next
        
        if not mergedList:
            return None
        
        mergedList = sorted(mergedList)[::-1]
        last = None
        
        for v in mergedList:
            last = ListNode(val=v, next=last)
        
        return last