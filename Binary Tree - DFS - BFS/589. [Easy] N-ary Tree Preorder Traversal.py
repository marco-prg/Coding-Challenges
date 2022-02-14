# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value.

# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        
        def dfs(root):
            nonlocal result
            
            if not root:
                return
            
            result.append(root.val)
            
            for r in root.children:
                dfs(r)
        
        dfs(root)
        return result


# Stack - Tree - Depth-First Search