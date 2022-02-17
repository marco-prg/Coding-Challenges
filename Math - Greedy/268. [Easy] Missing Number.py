# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        
        for i,v in enumerate(nums):
            result = result + i + 1 - v
            
        return result


# Array - Hash Table - Math - Bit Manipulation - Sorting