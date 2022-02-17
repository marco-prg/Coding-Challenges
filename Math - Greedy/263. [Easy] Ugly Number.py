# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.

class Solution:
    def isUgly(self, num: int) -> bool:
        if num < 1:
            return False
        
        for i in [2, 3, 5]:
            while num % i == 0:
                num //= i
                
        return num == 1


# Math