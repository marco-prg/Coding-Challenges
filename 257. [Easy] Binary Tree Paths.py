# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return self.thePath([], [], root)
    
    def thePath(self, result, current_path, root):
        if not root:
            return result
        
        separator = "->"
        c = [*current_path, root.val]
        
        if not root.left and not root.right:            
            result.append(separator.join(str(i) for i in c))
            return result
        
        result = self.thePath(result, c, root.left)
        return self.thePath(result, c, root.right)