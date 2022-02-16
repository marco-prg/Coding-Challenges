# Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
# In one move, you can increment n - 1 elements of the array by 1.

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # return sum(nums) - min(nums) * len(nums)
        
        result = 0        
        minimum = min(nums)
        
        for n in nums:
            result += n - minimum
            
        return result


# Array - Math