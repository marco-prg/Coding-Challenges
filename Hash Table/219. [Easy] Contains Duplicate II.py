# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        
        for i, v in enumerate(nums):
            if v in d and i - d[v] <= k:
                return True
            d[v] = i
        
        return False


# Array - Hash Table - Sliding Window