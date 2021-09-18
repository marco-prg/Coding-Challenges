# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, s: int) -> bool:        
        if not root:
            return False
        
        if root.val - s == 0 and not root.left and not root.right:
            return True
        
        return self.hasPathSum(root.left, s-root.val) or self.hasPathSum(root.right, s-root.val)
        