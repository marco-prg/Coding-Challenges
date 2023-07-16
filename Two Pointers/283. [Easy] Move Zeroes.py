# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Do not return anything, modify nums in-place instead.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pointer = 0

        for n in nums:
            if n:
                nums[pointer] = n
                pointer += 1
        
        for i in range(pointer, len(nums)):
            nums[i] = 0


# Array - Two Pointers