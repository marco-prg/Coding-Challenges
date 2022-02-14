# You have n coins and you want to build a staircase with these coins. 
# The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        result = 0
        
        while n > 0:
            n -= result + 1
            result += 1
            
        return result if n == 0 else result - 1


# Math - Binary Search   