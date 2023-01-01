# You are given an integer array nums and an integer target.
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
#  - For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

import collections

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Storing all values with corresponding counter
        elements = collections.defaultdict(int)
        # Initialization
        elements[0] = 1

        # Explanation: we want to obtain every possible value with the nums array
        # At each step, we store every value +/- the current nums value, then we forgot about the previous step
        # To avoid large arrays, we store for each value a key and a counter as a value in the dict, to store how many times we need to consider it

        for num in nums:
            # Defaultdict is safe when the key does not exists (default value = 0 for int)
            temp = collections.defaultdict(int)
            
            for elem,count in elements.items():
                temp[elem + num] += count
                temp[elem - num] += count
            
            elements = temp
        
        return elements[target]


# Array - Dynamic Programming - Backtracking


# Note: [Dynamic Programming] A naive approach to this problem is to use recursion, but as a result I got a TLE.
# Replacing the recursion with the for loops and Memoization did the trick
