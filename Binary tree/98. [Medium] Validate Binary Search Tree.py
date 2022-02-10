# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
#  - The left subtree of a node contains only nodes with keys less than the node's key.
#  - The right subtree of a node contains only nodes with keys greater than the node's key.
#  - Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root):
        output = []
        self.inOrder(root, output)
        
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False

        return True

    def inOrder(self, root, output):
        if not root:
            return
        
        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)


# Tree - Binary Tree - Binary Search Tree - Depth-First Search