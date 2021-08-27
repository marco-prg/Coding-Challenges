# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current_number = nums[0]
        seen_counter = 1
        
        for i in range(1, len(nums)):
            if nums[i] == current_number:
                seen_counter += 1
            else:
                if seen_counter == 1:
                    current_number = nums[i]
                else:
                    seen_counter -= 1
        
        return current_number
        