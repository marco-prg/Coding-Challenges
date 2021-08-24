# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()        
        
        search = [x for x in nums if x <= 0]
        
        for i in range(len(search)):
            r = self.twoSum(search[i], nums[i+1:])
            
            for x in r:
                if x not in result:
                    result.append(x)
                
        return result
    
    
    def twoSum(self, target, nums):
        result = []
        seen = {}
        
        for n in nums:
                       
            if seen.get(-n):
                result.append([*seen[-n], n]) 
                
            seen[n+target] = [target,n]
        
        return result