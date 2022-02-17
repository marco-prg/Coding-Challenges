# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))
        
        d = {}
        
        for n in nums:
            d[n] = d.get(n, 0) + 1
        
        return max(d.values()) != 1


# Array - Hash Table - Sorting