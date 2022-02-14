# Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a = ''.join([str(n) for n in nums])
        a = a.split('0')
        return max([len(x) for x in a])


# Array