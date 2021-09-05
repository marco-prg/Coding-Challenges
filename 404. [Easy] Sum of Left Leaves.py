# Given the root of a binary tree, return the sum of all left leaves.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.theSum(root)
        return self.result
    
    def theSum(self, root):
        if not root:
            return
        
        left = root.left
        if left and not left.left and not left.right:
            self.result += left.val
        
        self.theSum(root.right)        
        self.theSum(root.left)
        