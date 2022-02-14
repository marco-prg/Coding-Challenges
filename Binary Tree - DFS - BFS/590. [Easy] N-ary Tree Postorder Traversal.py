# Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value.

# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        
        r = [root] if root else False
        
        while r:
            node = r.pop()
            result.append(node.val)
            r.extend([c for c in node.children if node.children])
        
        result.reverse()
        return result


# Stack - Tree - Depth-First Search