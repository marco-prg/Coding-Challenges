# Given an integer array nums, return the third distinct maximum number in this array. 
# If the third maximum does not exist, return the maximum number.

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        one = two = three = float("-inf")
        
        for n in nums:
            if n > one:
                one, two, three = n, one, two
            elif n < one and n > two:
                two, three = n, two
            elif n < two and n > three:
                three = n
        
        return three if three > float("-inf") else one
    

# Array - Sorting