# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        
        if not nums:
            return result
        
        # Two binary searches (Explanation: page 149 Skiena)
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (right + left) // 2
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        if nums[left] != target:
            return result
        
        result[0] = left
        # We don't have to set left to 0 this time
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] <= target:
                left = mid + 1
            else: 
                right = mid - 1
        
        result[1] = right
        
        return result


# Array - Binary Search