# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:        
        if not root:
            return 0
        
        l = 1
        r = 1
        
        if root.left:
            l += self.minDepth(root.left)
        if root.right:
            r += self.minDepth(root.right)
            
        if l == 1:
            return r
        if r == 1:
            return l
            
        return min(l, r)


# Tree - Binary Tree - Depth-First Search - Breadth-First Search