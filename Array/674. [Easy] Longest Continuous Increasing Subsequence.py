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

# Sliding Window solution:
# Every (continuous) increasing subsequence is disjoint, and the boundary of each such subsequence occurs whenever nums[i-1] >= nums[i].
# When it does, it marks the start of a new increasing subsequence at nums[i], and we store such i in the variable anchor.

# class Solution:
#     def findLengthOfLCIS(self, nums: List[int]) -> int:
#         ans = anchor = 0
#         for i in range(len(nums)):
#             if i and nums[i-1] >= nums[i]:
#                 anchor = i
#             ans = max(ans, i - anchor + 1)
#         return ans


# Array