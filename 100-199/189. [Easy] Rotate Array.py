# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Follow up:
# -  Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# -  Could you do it in-place with O(1) extra space?

# Do not return anything, modify nums in-place instead.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % len(nums)
        j = 0
        
        while n > 0 and k % n != 0:
            
            for i in range(0, k):
                nums[j + i], nums[len(nums) - k + i] = nums[len(nums) - k + i], nums[j + i]     # swap
                
            j += k                
            n -= k            
            k = k % n