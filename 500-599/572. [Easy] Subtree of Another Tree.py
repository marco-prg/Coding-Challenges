# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Alternative approach: we can convert our tree into string representation, and then just check if the substring exists in the target string.
# class Solution(object):
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:        
#         def convert(p):
#             return "^" + str(p.val) + "#" + convert(p.left) + convert(p.right) if p else "$"        
#         return convert(t) in convert(s)

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        check = False        
        if root.val == subRoot.val:
            check = self.identical(root, subRoot)        
        
        return check or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def identical(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if (root and not subRoot) or (not root and subRoot):
            return False
        
        if root.val != subRoot.val:
            return False
        
        return self.identical(root.left, subRoot.left) and self.identical(root.right, subRoot.right) 