# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        # Target == 0, so we need at least 1 number <= 0
        nums.sort()  
        negative = [x for x in nums if x <= 0]
        
        for i in range(len(negative)):
            # nums is sorted, so we can use the index i like this:
            self.twoSum(negative[i], nums[i+1:], result)
                
        return result
    
    
    def twoSum(self, current, nums, result):
        seen = set()
        
        for n in nums:                       
            if -n in seen:
                result.add((current, -(current + n), n))                
            seen.add(current + n)


# Array - Two Pointers - Sorting