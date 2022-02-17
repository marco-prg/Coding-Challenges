# You are given a sorted unique integer array nums.
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
# That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:
# -  "a->b" if a != b
# -  "a" if a == b

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        
        if not nums:
            return result
        
        start = end = nums[0]
        nums = nums[1:] + [nums[-1]]
        
        for n in nums:           
            if n != end + 1:
                result.append(str(start) + ("->" + str(end)) * (start != end))                    
                start = n
            end = n
        
        return result


# Array