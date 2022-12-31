# Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.
# Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.
# Note that you need to maximize the answer before taking the mod and not after taking it.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.result = -1

        def postorder_traversal(node: Optional[TreeNode]):
            if not node:
                return 0
            # Value of the current subtree
            current_value = postorder_traversal(node.left) + postorder_traversal(node.right) + node.val
            if self.result != -1:
                # We try this subtree vs the remaining part and perform the multiplication to update the result so far (maximum product)
                self.result = max(self.result, current_value * (total_sum - current_value))
            return current_value     
        
        # First traversal to get the sum of all node values
        total_sum = postorder_traversal(root)
        self.result = 0
        # Now that we have the total_sum, we can traverse the tree again in order to perform the comparisons   
        postorder_traversal(root)

        return self.result % (10 ** 9 + 7)


# Tree - Depth-First Search - Binary Tree - Dynamic Programming
