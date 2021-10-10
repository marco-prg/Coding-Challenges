# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
# A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

import collections

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        result = 0
        c = collections.Counter(nums)
        for k,v in c.items():
            result = max(result, (c[k+1] or -v) + v)
            
        return result