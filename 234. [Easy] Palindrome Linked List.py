# Given the head of a singly linked list, return true if it is a palindrome.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a = []        
        while head:
            a.append(head.val)
            head = head.next
            
        h = len(a) // 2            
        m = len(a) % 2
        return a[:h+m] == a[h:][::-1]
        