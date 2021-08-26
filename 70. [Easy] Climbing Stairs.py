# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Solution: Fibonacci - dynamic programming

class Solution:
    def climbStairs(self, n: int) -> int:
        result = [0, 1, 2]
        
        for i in range(3, n+1):
            result.append(result[-1] + result[-2])
            
        return result[n]