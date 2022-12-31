# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack_dfs(current_index, current_subset):            
            result.append(current_subset)
            
            for i in range(current_index, len(nums)):
                # use next integers to complete the combination
                backtrack_dfs(i + 1, [nums[i]] + current_subset)
        
        result = []        
        backtrack_dfs(0, [])

        return result


# More explicit version
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first, current_subset):
            # if the combination is done
            if len(current_subset) > len(nums):                
                return
            
            result.append(current_subset.copy())
            
            for i in range(first, n):
                # add nums[i] into the current combination
                current_subset.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, current_subset)
                # backtrack
                current_subset.pop()
        
        result = []
        n = len(nums)
        
        backtrack(0, [])

        return result


# Array - Backtracking - Bit Manipulation
