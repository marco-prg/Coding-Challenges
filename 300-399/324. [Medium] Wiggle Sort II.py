# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3] ... .
# You may assume the input array always has a valid answer.

# Do not return anything, modify nums in-place instead
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        half = len(nums) // 2 + len(nums) % 2   # or len(nums[::2])

        # [::2] -> odd positions (1°, 3° ... - indexes: 0, 2 ...), [1::2] -> even positions
        # Reverse ([::-1]) required in order to avoid having adjacent numbers with the same value
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]