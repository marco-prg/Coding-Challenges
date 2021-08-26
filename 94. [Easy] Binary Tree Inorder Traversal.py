# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        if not root:
            return result
        
        left = self.inorderTraversal(root.left)
        
        if root.val:
            left.append(root.val)
        
        left.extend(self.inorderTraversal(root.right))
        return left