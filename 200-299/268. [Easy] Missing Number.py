# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        
        for num in range(1, len(nums) + 1):
            result += num
            
        for num in nums:
            result -= num
            
        return result