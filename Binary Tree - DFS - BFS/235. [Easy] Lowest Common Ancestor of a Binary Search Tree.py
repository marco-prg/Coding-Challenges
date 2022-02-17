# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
# According to the definition of LCA on Wikipedia:
# “The lowest common ancestor is defined between two nodes p and q as the lowest node in T 
# that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':        
        minimum = min(p.val, q.val)
        maximum = max(p.val, q.val)
        val = root.val
        
        if minimum <= val and val <= maximum:
            return root
        
        if maximum < val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if minimum > val:
            return self.lowestCommonAncestor(root.right, p, q)


# Tree - Binary Tree - Binary Search Tree - Depth-First Search        