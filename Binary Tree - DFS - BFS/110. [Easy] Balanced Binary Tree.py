# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.height(root) >= 0        
        
    def height(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        if root.left == None and root.right == None:
            return 1
        
        l = self.height(root.left)
        r = self.height(root.right)
        
        if abs(l - r) > 1 or l < 0 or r < 0:
            return -1       
        
        return 1 + max(l,r)       


# Tree - Binary Tree - Depth-First Search        