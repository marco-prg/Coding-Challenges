# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = 0   
        
        for elems in [l1, l2]:
            index = 0
            while elems:
                result += elems.val * (10 ** index)
                elems = elems.next
                index = index + 1
                
        previous = ListNode(str(result)[0])
        current = None
        
        for digits in str(result)[1:]:
            current = ListNode(digits)
            current.next = previous
            previous = current
        
        return current if current else previous