# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]        
        if not nums:
            return result 
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (right + left) // 2
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        result[0] = left
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] <= target:
                left = mid + 1
            else: 
                right = mid - 1
        
        result[1] = right
        
        return result if result[0] <= result[1] else [-1, -1]