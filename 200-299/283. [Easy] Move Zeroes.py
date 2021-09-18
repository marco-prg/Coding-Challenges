# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Do not return anything, modify nums in-place instead.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pointer = 0
        
        for i,v in enumerate(nums):
            if v:
                nums[i + pointer] = v
            else:
                pointer -= 1
                
        for i in range(-1, pointer - 1, -1):
            nums[i] = 0