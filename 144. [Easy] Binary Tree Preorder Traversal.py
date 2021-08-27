# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        if not root:
            return result
        
        if root.val:
            result.append(root.val)
            
        result.extend(self.preorderTraversal(root.left))
        result.extend(self.preorderTraversal(root.right))
        
        return result
        