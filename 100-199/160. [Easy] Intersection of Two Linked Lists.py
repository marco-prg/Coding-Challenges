# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
# If the two linked lists have no intersection at all, return null.
# Note that the linked lists must retain their original structure after the function returns.

# Custom Judge:
# The inputs to the judge are given as follows (your program is not given these inputs):
# -  intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
# -  listA - The first linked list.
# -  listB - The second linked list.
# -  skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
# -  skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
# The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program.
# If you correctly return the intersected node, then your solution will be accepted.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = []
        b = []
        
        headC = headA
        
        if not headA or not headB:
            return None
        
        while headA:
            a.append(hex(id(headA)))
            headA = headA.next
        
        while headB:
            b.append(hex(id(headB)))
            headB = headB.next
        
        intercept = False
            
        while a[-1] == b[-1]:
            intercept = True
            a = a[:-1]
            b = b[:-1]
            
            if not len(a) or not len(b):
                break
        
        if not intercept:
            return None
        
        lenA = len(a)
        
        for i in range(lenA):
            headC = headC.next
            
        return headC