# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        result = [0, 1, 2]

        # Solution: Fibonacci - Dynamic Programming        
        for _ in range(3, n+1):
            result.append(result[-1] + result[-2])
            
        return result[n]


# Math - Dynamic Programming - Memoization