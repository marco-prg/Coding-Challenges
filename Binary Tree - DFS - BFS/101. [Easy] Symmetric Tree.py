# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.checkSymmetric([root])
    
    def checkSymmetric(self, array: List[TreeNode]) -> bool:        
        nodes = []
        values = []

        # Check all values of current level (saved in 'values')
        # Deeper level nodes stored in 'nodes' for next recursion        
        for node in array:
                values.append(node.val if node else None)
                if node:
                    nodes.append(node.left)
                    nodes.append(node.right)

        # Check current level symmetry
        mid = len(values) // 2            
        result = values[:mid + len(values) % 2] == values[mid:][::-1]        
        
        # Check if it is the deepest level  
        end = not any(nodes)
        
        # Or not symmetric
        if end or not result:
            return result
        else:
            return self.checkSymmetric(nodes)


# Tree - Depth-First Search - Breadth-First Search - Binary Tree
        