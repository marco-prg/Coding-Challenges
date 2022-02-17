# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:        
        if not root:
            return 0
        
        l = 1
        r = 1
        
        if root.left:
            l += self.maxDepth(root.left)
        
        if root.right:
            r += self.maxDepth(root.right)
            
        return max(l, r)


# Tree - Binary Tree - Depth-First Search - Breadth-First Search