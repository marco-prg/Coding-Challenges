# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        
        for n in nums:
            t = abs(n) - 1
            if nums[t] > 0:
                nums[t] *= -1
        
        
        for k,v in enumerate(nums):
            if v > 0:
                result.append(k + 1)
                
        return result