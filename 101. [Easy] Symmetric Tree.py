# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.the_symmetric([root])
    
    def the_symmetric(self, array: List[TreeNode]) -> bool:
        
        values = []
        check = []
        
        for node in array:
                check.append(node.val if node else None)
                values.append(node.left if node else None)
                values.append(node.right if node else None)
            
        the_end = True
            
        for v in values:
            if v != None:
                the_end = False
                break
        
        lun = len(check) // 2
        if lun == 0:
            lun = 1
            check.append(check[0])
        
        if the_end:
            return check[:lun] == check[lun:][::-1]
        else:
            return self.the_symmetric(values) if check[:lun] == check[lun:][::-1] else False
        