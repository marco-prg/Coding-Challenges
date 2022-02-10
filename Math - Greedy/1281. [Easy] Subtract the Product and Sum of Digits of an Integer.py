# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

# from math import prod
# 
# class Solution:
#     def subtractProductAndSum(self, n: int) -> int:
#         digits = [int(d) for d in str(n)]
#         return prod(digits) - sum(digits)

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0
        
        while n:
            t = n % 10
            p *= t
            s += t
            n //= 10
        
        return p - s


# Math