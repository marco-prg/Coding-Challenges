# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))
        
        d = {}
        
        for n in nums:
            if d.get(n):
                d[n] += 1
            else:
                d[n] = 1
        
        return max(d.values()) != 1