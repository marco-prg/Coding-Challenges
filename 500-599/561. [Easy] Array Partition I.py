# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) 
# such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()        
        return sum(v for i,v in enumerate(nums) if not i % 2)