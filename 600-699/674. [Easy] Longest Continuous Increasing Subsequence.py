# Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). 
# The subsequence must be strictly increasing.
# A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 
# and for each l <= i < r, nums[i] < nums[i + 1].

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:        
        result = 0        
        current = nums[0] - 1
        value = 0
        
        for num in nums:            
            if num > current:                
                value += 1                
            else:                   
                result = max(result, value)
                value = 1
            
            current = num
        
        result = max(result, value)
        return result