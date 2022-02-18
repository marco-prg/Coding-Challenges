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
        
        for elem in [l1, l2]:
            index = 0
            while elem:
                result += elem.val * (10 ** index)
                elem = elem.next
                index += 1
                
        current = None        
        for i in str(result):
            previous = current
            current = ListNode(i)
            current.next = previous
        
        return current


# Linked List - Math - Recursion