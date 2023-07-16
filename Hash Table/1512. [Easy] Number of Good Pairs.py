# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = {}
        result = 0

        for n in nums:
            if n in seen:
                result += seen[n]
            
            seen[n] = seen.get(n, 0) + 1
        
        return result


# Array - Hash Table - Math - Counting