# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxi = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        self.thePath(root)
        return self.maxi
    
    def thePath(self, root):
        l = self.thePath(root.left) + 1 if root.left else 0
        r = self.thePath(root.right) + 1 if root.right else 0
        
        self.maxi = max(self.maxi, l+r)        
        return max(l, r)