# Given the root of a binary tree, return the sum of every tree node's tilt.
# The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. 
# If a node does not have a left child, then the sum of the left subtree node values is treated as 0. 
# The rule is similar if there the node does not have a right child.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.result = 0  
        self.postOrder(root)
        return self.result
    
    def postOrder(self, root):
            if not root:
                return            
            
            self.postOrder(root.left)
            self.postOrder(root.right)
            
            l = root.left.val if root.left else 0
            r = root.right.val if root.right else 0
            
            self.result += abs(l-r)            
            root.val += l + r


# Tree - Binary Tree - Depth-First Search